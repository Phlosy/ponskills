#!/usr/bin/env bash
# ==============================================================================
# Ensure all third-party companion skills required by
# `academic-proposal-defense-workflow` (inside `ponskills`) are present in the
# workspace's `third_party_skills/` directory (similar to pulling third-party
# libraries in software projects).
#
# Usage:
#   bash ponskills/academic-proposal-defense-workflow/scripts/ensure_dependent_skills.sh --check
#   bash ponskills/academic-proposal-defense-workflow/scripts/ensure_dependent_skills.sh --install
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
PONSKILLS_ROOT="$(cd "${SKILL_ROOT}/.." && pwd)"
WORKSPACE_ROOT="$(cd "${PONSKILLS_ROOT}/.." && pwd)"

# Default third-party skills directory in the workspace (can be overridden via THIRD_PARTY_SKILLS_DIR)
THIRD_PARTY_DIR="${THIRD_PARTY_SKILLS_DIR:-${WORKSPACE_ROOT}/third_party_skills}"

MODE="${1:---check}"

# Canonical Git repositories for third-party companion skills
EVOSKILLS_REPO="https://github.com/EvoScientist/EvoSkills.git"
HUMANIZER_REPO="https://github.com/blader/humanizer.git"
PPT_MASTER_REPO="https://github.com/hugohe3/ppt-master.git"
ASTROPRISM_REPO="git@git.dslab.cc:dslab/astroprism/astroprism.git"

missing=0

check_or_clone() {
  local name="$1"
  local primary_dir="$2"
  local fallback_dir_1="$3"
  local fallback_dir_2="$4"
  local repo_url="$5"

  if [[ -d "${primary_dir}" ]]; then
    echo "[OK] ${name} found at: ${primary_dir}"
    return 0
  elif [[ -n "${fallback_dir_1}" && -d "${fallback_dir_1}" ]]; then
    echo "[OK] ${name} found at fallback: ${fallback_dir_1}"
    return 0
  elif [[ -n "${fallback_dir_2}" && -d "${fallback_dir_2}" ]]; then
    echo "[OK] ${name} found at fallback: ${fallback_dir_2}"
    return 0
  fi

  if [[ "${MODE}" == "--install" ]]; then
    mkdir -p "${THIRD_PARTY_DIR}"
    echo "[INSTALL] Cloning ${name} from ${repo_url} -> ${primary_dir} ..."
    git clone --depth 1 "${repo_url}" "${primary_dir}"
    echo "[OK] Installed ${name} at: ${primary_dir}"
  else
    echo "[MISSING] ${name} not found (expected ${primary_dir}). Repo: ${repo_url}"
    missing=$((missing + 1))
  fi
}

echo "=== Checking Third-Party Companion Skills (Target: ${THIRD_PARTY_DIR}) ==="
check_or_clone "EvoSkills" \
  "${THIRD_PARTY_DIR}/EvoSkills" \
  "${WORKSPACE_ROOT}/../skills/EvoSkills" \
  "${PONSKILLS_ROOT}/third_party_skills/EvoSkills" \
  "${EVOSKILLS_REPO}"

check_or_clone "humanizer" \
  "${THIRD_PARTY_DIR}/humanizer" \
  "${WORKSPACE_ROOT}/../skills/humanizer" \
  "${PONSKILLS_ROOT}/third_party_skills/humanizer" \
  "${HUMANIZER_REPO}"

check_or_clone "ppt-master" \
  "${THIRD_PARTY_DIR}/ppt-master" \
  "${WORKSPACE_ROOT}/../skills/ppt-master" \
  "${PONSKILLS_ROOT}/third_party_skills/ppt-master" \
  "${PPT_MASTER_REPO}"

if [[ -d "${THIRD_PARTY_DIR}/docx-template-report" ]]; then
  echo "[OK] docx-template-report found at: ${THIRD_PARTY_DIR}/docx-template-report"
elif [[ -d "${WORKSPACE_ROOT}/../skills/docx-template-report" ]]; then
  echo "[OK] docx-template-report found at fallback: ${WORKSPACE_ROOT}/../skills/docx-template-report"
elif [[ "${MODE}" == "--install" ]]; then
  mkdir -p "${THIRD_PARTY_DIR}"
  echo "[INSTALL] Fetching docx-template-report from ${ASTROPRISM_REPO} -> ${THIRD_PARTY_DIR}/docx-template-report ..."
  tmp_dir="$(mktemp -d)"
  if git clone --depth 1 --filter=blob:none --sparse "${ASTROPRISM_REPO}" "${tmp_dir}" && git -C "${tmp_dir}" sparse-checkout set skills/docx-template-report; then
    cp -R "${tmp_dir}/skills/docx-template-report" "${THIRD_PARTY_DIR}/docx-template-report"
    echo "[OK] Installed docx-template-report at: ${THIRD_PARTY_DIR}/docx-template-report"
  fi
  rm -rf "${tmp_dir}"
else
  echo "[MISSING] docx-template-report not found at ${THIRD_PARTY_DIR}/docx-template-report (upstream: ${ASTROPRISM_REPO} :: skills/docx-template-report)"
  missing=$((missing + 1))
fi

if [[ "${missing}" -gt 0 && "${MODE}" != "--install" ]]; then
  echo "Run 'bash ${BASH_SOURCE[0]} --install' to automatically create ${THIRD_PARTY_DIR} and clone missing third-party skill repositories."
  exit 1
fi

echo "=== All third-party companion skill checks completed ==="

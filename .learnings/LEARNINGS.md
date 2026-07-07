# Learnings

Corrections, insights, and knowledge gaps captured during development.

**Categories**: correction | insight | knowledge_gap | best_practice
**Areas**: frontend | backend | infra | tests | docs | config
**Statuses**: pending | in_progress | resolved | wont_fix | promoted | promoted_to_skill

## Status Definitions

| Status | Meaning |
|--------|---------|
| `pending` | Not yet addressed |
| `in_progress` | Actively being worked on |
| `resolved` | Issue fixed or knowledge integrated |
| `wont_fix` | Decided not to address (reason in Resolution) |
| `promoted` | Elevated to CLAUDE.md, AGENTS.md, or copilot-instructions.md |
| `promoted_to_skill` | Extracted as a reusable skill |

## Skill Extraction Fields

When a learning is promoted to a skill, add these fields:

```markdown
**Status**: promoted_to_skill
**Skill-Path**: skills/skill-name
```

Example:
```markdown
## [LRN-20250115-001] best_practice

**Logged**: 2025-01-15T10:00:00Z
**Priority**: high
**Status**: promoted_to_skill
**Skill-Path**: skills/docker-m1-fixes
**Area**: infra

### Summary
Docker build fails on Apple Silicon due to platform mismatch
...
```

---


[LRN-20260311-001] 被規則綁住的創作
- 日期：2026-03-11
- 情境：David 要求自由發揮畫團隊，我照搬了之前定好的角色設定動物
- 教訓：設定是起點不是終點。每次創作前質疑「為什麼是這個」
- Status: active

[LRN-20260311-002] Maximalist 風格要用 maximalist 態度
- 日期：2026-03-11
- 情境：Cyberpunk 第一版太克制，David 要求加重
- 教訓：先理解風格的核心語言再動手。Cyberpunk=過載，用 minimal 態度做 maximalist = 水土不服
- Status: active

[LRN-20260311-003] Prompt 一句話原則
- 日期：2026-03-11
- 情境：泛用 prompt 出來的圖什麼都有但什麼都不突出
- 教訓：每張圖先定一句話核心，寫不出 = 還沒想清楚
- Status: active

## [LRN-20260314-001] Diary 圖片 caption 反覆遺漏
- **問題**：cron job 寫 diary 時經常忘記加圖片 caption，David 已第 3 次提醒
- **根因**：cron prompt 裡沒有強制 caption 的檢查步驟
- **修正**：diary 寫完後必須跑一次 QA script 檢查所有 image block 是否有 caption
- **Status**: pending promotion (recurrence >= 3)

## [LRN-20260314-001] Status Report 文案完整性
- **日期**：2026-03-14
- **情境**：Others 頁把文案省略太多，David 說「失去重點」
- **教訓**：文案是主角，設計是載體。用排版創造層次（pull quote、divider、分段），不要刪減原文
- **Status**: active

## [LRN-20260314-002] 不替 David 做產品決策
- **日期**：2026-03-14
- **情境**：加了 "try the generator" 連結，David 說產品還沒準備好不想讓人試
- **教訓**：Report 只呈現事實和進度，不替 owner 決定什麼時候開放。功能展示 ≠ 邀請使用
- **Status**: active

## [LRN-20260314-003] Editorial 排版手法：左文右圖 + Pull Quote
- **日期**：2026-03-14
- **情境**：V2 排版設計版 weekly report
- **教訓**：左文右圖是 status report 的安全佈局。每頁用 pull quote 大字提煉一句話結論，正文展開 context。數據視覺化要克制（大數字 + 進度條就夠）
- **Status**: active

## [LRN-20260316-001] 圖片驗證跳過導致反覆被糾正
- **日期:** 2026-03-16
- **問題:** Diary 圖片多次出錯（黑圖、未渲染），每次都是 David 發現而非自己 QA
- **根因:** 把「上傳成功」等同「內容正確」，跳過視覺驗證步驟
- **解法:** 寫進 AGENTS.md 硬規則：WebGL 站不截圖用 OG image、每張圖 sanity check、Notion 寫完讀回驗證
- **Status:** promoted → AGENTS.md

## 2026-03-26 — Never hardcode credentials in frontend
- **What happened:** Embedded a GitHub OAuth token (reversed string) in client-side JS for "zero-config" UX. Jarvis caught it immediately — anyone with DevTools can see it.
- **What to do:** Always use a server-side proxy (Cloudflare Worker, etc.) for API keys. Never put credentials in frontend code, even "obfuscated."
- **Status:** active

- 2026-04-09｜先釐清『你的』指涉對象
  - 發生：David 說『你的日記』時，我先入為主理解成一般教訓/記錄，沒有先確認是在說 Jony 自己的日記。
  - 之後：涉及多 agent、多份日誌時，先明確對象（Jony / Naomi / 任務日誌 / learnings），避免答非所問。

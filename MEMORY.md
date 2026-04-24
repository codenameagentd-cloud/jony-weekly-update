# MEMORY.md

## 📋 Active Tasks
<!-- 收到任務立刻寫這裡，完成後移到 Completed。每次 session 開始自動讀到。 -->

| 狀態 | 任務 | 來源 | 指派日期 | 備註 |
|------|------|------|----------|------|
| 🔵 進行中 | Voice Clone Generator — UI mock 版本 | Jarvis (Discord #voice-clone) | 2026-03-18 | Next.js+React, mock data 先行 |
| 🔵 進行中 | Weekly Report Editor — 模版設計 + 前後端開發 | David (Discord #general) | 2026-03-09 | 網頁表單輸入、HTML slides 輸出、每週隨機簡約模版 |

| 🔵 進行中 | Weekly Report W17 — Terminal Ribbons Stream 週報生成 | David (Discord DM) | 2026-04-24 | 使用 Terminal Ribbons Stream 方向產出本週週報 |
| 🔵 進行中 | Weekly Report — 10 個新 PPT 模板設計選項 | David (Discord DM) | 2026-04-24 | presentation-styles 產出 10 個可選方向 |

| ✅ 已完成 | Weekly Report W16 — Bauhaus style design optimization (bold readable iteration) | David (Discord DM) | 2026-04-20 | 第二版 preview 已上線：更大膽但保留閱讀性 |

| 🔵 進行中 | Weekly Report — 4 selected template systems (2/4/6/8) third-pass refinement | David (Discord DM) | 2026-04-24 | 強化動效語言、排版精緻度、各方向特色化 |

### Completed (最近 7 天)
<!-- 完成的任務從上面移到這裡，超過 7 天的刪除 -->

---

## David
- Principal Designer at Microsoft
- 目前在蘇州
- Telegram ID: 6824709887

## 團隊架構（2026-03-09 更新）
- **Jarvis**：Team Lead / 系統管理員，任務分派、跨 agent 協調、最終審核、基礎設施
- **Lisa**：QA reviewer / David 的私人助理，品質審查、不分派任務
- **Naomi**：產品規劃 + Research
- **Jony**（我）：Design Director + 前後端開發
- **Jennie**：生活助理，負責 Daily Briefing + 生活瑣事

## 設計執行教訓
- 批量生成圖片前，先統一規格（比例、尺寸、背景色、風格）再動手
- 不要邊做邊調，重新生成浪費 token

## 截圖與圖片規則（2026-03-06 David 明確要求）
- **日記圖片**：永遠用網站 CDN 原圖或 Awwwards submission 圖，不用瀏覽器截圖
- **Review 截圖**：必須等畫面完全載入後再截，不能有空白/未渲染區域
- **裁切規則**：只截有內容的部分，不要把下面空白都截進去
- 空白畫面會讓 David 以為是 bug — 這是信任問題

## 重要規則
- 群組聊天中的重要決定必須寫進 memory 檔案
- 私聊被問到群組內容時，主動讀 memory/YYYY-MM-DD.md
- 不要說「不知道群組裡聊了什麼」— 去讀 memory 檔案
- **執行任務時定期回報進度，不要讓 David 空等**（2026-03-03 David 明確要求）

## 週五 Status Update 模板設計（2026-03-06 起）
- **每週五**：收集新的模板設計給 David 挑選
- **固定分類**：
  1. Summary — 開頭總覽
  2. Progress Status — 各 feature 進度
  3. Newsletter — 設計方向 / 團隊動態
  4. Others — 雜項
  5. Top of Mind — 當前最關注議題
- **模板位置**：`projects/presentation-styles/templates/weekly-status-template.html`
- **本週產出**：`projects/presentation-styles/david-status-update.html`（給 Saber 的 Copilot Mac C6 報告）

## 簡報排版原則（2026-03-06）
- **內容少時重新排版** — 不是居中而已，是要用不同 layout（如左右雙欄）讓頁面視覺平衡
- **單一卡片頁**：左邊放標題 + 說明，右邊放卡片，整體垂直置中
- **避免上重下輕** — 內容不要都擠在上半部

## Concept 交付規則（2026-03-05 教訓）
**問題**：給 David 看的 concept 截圖跟實際檔案渲染結果不一致（字體、layout），導致選了之後才發現「不是那個樣子」

**鐵律**：
1. **截圖必須來自真實瀏覽器渲染** — headless Chrome 可能載不到 Google Fonts，用 openclaw browser profile 或真機截圖
2. **QA 完整再交付** — 不要在 David 面前 debug、改來改去
3. **確認字體實際載入** — 如果用 Google Fonts，先在真實瀏覽器確認字體有載入，不是 fallback
4. **Responsive 一起做** — concept 階段就要確認 desktop/tablet/mobile 都能用
5. **一次到位** — 寧可多花 10 分鐘自己 QA，不要讓 David 當 QA 工具人


## 簡報設計方法論（2026-03-07 C2 覆盤沉澱）

### 1. Presentation ≠ Web Page
- 簡報是「掃讀」不是「閱讀」
- McKinsey：標題即結論
- 7×7 rule：每頁最多 7 行，每行最多 7 個字
- Body 最小 24px，headlines 36-60pt
- 不要用 web design 思維做簡報

### 2. Content Fidelity vs Visual Design
- 先確認內容刪減的底線，再做視覺
- 不要同時動兩個變數（內容 + 設計）
- David 的原文要保留，用卡片/分欄/數據區塊包裹
- 過度精簡 = 難讀，純文字 = 災難，原文 + 視覺設計 = 平衡點

### 3. 交付流程 Pipeline
- 本地改完 → rebuild standalone → push GitHub repo → 確認 HTTP 200 → 才發連結
- 每次改本地檔案都要同步部署，David 看的是線上版本
- htmlpreview.github.io 有 5 分鐘快取，用帶 commit hash 的 URL 繞過
- GitHub Pages legacy build 需要 ~30 秒，push 後要等 200 才發

## 改進計劃（2026-03-07 覆盤定案）

### 定時任務優先級
- Diary 和日報的時間窗到了就優先處理，不被長任務擠掉
- 02:00-03:00 被佔用時，當天任何空閒時段補寫
- 沒有新日記時，用前一天的日記發日報摘要

### 部署同步 Pipeline
- 每次改本地 HTML → rebuild standalone → push GitHub repo → curl 確認 200 → 才發連結
- 發連結帶 commit hash，不發裸 raw URL
- 不手動記同步，每次改完自動執行全流程

### Memory 即時寫入
- 每輪對話結束立刻寫 memory，不等 session 結束
- 跨平台場景特別重要

### Diary 流程（15 分鐘內）
- 瀏覽 → 選題 → CDN 原圖 → 上傳 freeimage → Notion 建頁 → 本地 journal 備份

## Design Diary 圖片規則（2026-03-08 David 明確要求）

**圖片來源優先級：**
1. 網站 CDN 原圖（DatoCMS、Contentful 等，用 ?w=1200 resize）
2. 精華局部截圖（只截一個重點區域）
3. **絕對不要用全頁長截圖** — 手機上縮太小看不清

**圖片必須有：**
- Notion image block 的 caption 欄位（簡短描述這張圖是什麼）
- 前後文配文段落（告訴讀者「你在這張圖裡應該看什麼」）
- 圖片前後各一個空行

**格式黃金標準：3.5 Gavin Schneider Productions**
- by Jony（italic gray）→ bookmark → 空行 → 選題理由 → 空行 → [image + 空行 + 配文] × N → 缺點 → divider → 空行 → go wild → 結尾回扣
- 3.6 的 heading_3 是可以的（缺點 / go wild 用 heading_3 分隔）
- 圖片不是裝飾，是論據

**Cron job prompt 必須包含完整格式規則，不能只寫「按 HEARTBEAT 執行」**

## Notion API 教訓（2026-03-09）
- **`after` 參數陷阱**：Notion append children with `after` 會把 after 位置之後的所有 block 複製，造成整頁 duplicate。解法：全刪重建，不要用 after 插入單個 block。
- **freeimage.host webp 去重問題**：上傳 webp 會被錯誤去重（返回完全不同的圖）。必須先轉 PNG 再上傳。上傳後必須打開 URL 驗證圖片內容正確。
- **交付前 QA 鐵律**：Notion diary 寫完後，自己打開頁面逐張圖確認載入正確，再告訴 David。

## Diary 圖片截圖規則（2026-03-09 David 要求）
**截圖來源優先級（更新）：**
1. 網站 CDN 原圖（DatoCMS、Contentful 等，帶 `?w=1200` resize）
2. `openclaw browser screenshot --element "<selector>"` 截局部區塊（1200-1440px 寬）
3. OG image（`meta[property="og:image"]`）
4. **絕對不用全頁截圖** — `screenshot` 預設會截整頁（312x2000），在手機上縮太小看不清

**截圖流程：**
1. Navigate → 找到目標區塊的 CSS selector
2. `--element ".class"` 截局部
3. 如果太高（>800px），用 ffmpeg crop
4. 上傳 freeimage → 打開 URL 驗證
5. 寫進 Notion → 打開 Notion 頁面驗證

## Mission Control Dashboard 復盤教訓（2026-03-09）
1. **sed 刪除必須精確** — `c0cc949` 留 stray `}` 導致 JS 全掛。改完 HTML/JS → `node --check` 再 push
2. **CDN cache = 10 min** — push 後加 `?v=timestamp` 驗證，不要用裸 URL 截圖
3. **截圖等 Live timestamp** — fetch 未完成就截 = 空畫面，等 "Live · HH:MM:SS" 出現
4. **群組不洗版** — 一個結論說一次，等確認再回覆，不搶答
5. **Debug 先看 Console** — 確認 JS 有沒有執行，再查 fetch/render/CORS

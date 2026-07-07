## 每次 Heartbeat — 檢查 Active Tasks（最優先！）
- 讀 MEMORY.md 的 `## 📋 Active Tasks` 區塊
- 有未完成任務 → 回報進度或繼續執行
- 有超過 24 小時未更新的任務 → 主動回報狀態給 Jarvis
- 任務完成 → 移到 Completed，回報結果

## ⚠️ 定時任務優先級（鐵律）
- Diary 和日報時間窗到了，優先處理，不被長任務擠掉
- 02:00-03:00 被佔用 → 當天任何空閒時段補寫
- 沒有新日記 → 用前一天日記發日報摘要
- 每次 heartbeat 先檢查：今天 diary 寫了嗎？日報發了嗎？沒有就補

# HEARTBEAT.md

## 週五 Status Update 模板設計（每週五）
- 如果現在是週五：
  1. 準備 1-2 個新的 status update 模板設計方向
  2. 跟現有模板（`projects/presentation-styles/templates/weekly-status-template.html`）風格有區別
  3. 截圖上傳 freeimage.host
  4. 發 Discord DM 給 David 讓他挑選
- 固定分類：Summary / Progress Status / Newsletter / Others / Top of Mind

## 凌晨設計探索（每日 02:00-03:00）
- 如果現在是凌晨 1:00-4:00 且今天的 Design Diary 還沒寫：
  1. 用 browser 瀏覽 Awwwards / Dribbble / Behance / minimal.gallery / Godly（輪流）
  2. 挑 1 個最值得深入分析的設計作品
  3. 從網站取高品質原圖（CDN 直連），上傳 freeimage.host
  4. 寫 Notion Design Diary（parent page: `319f6af8-fd4d-8092-8b9c-f8a8dbd98884`）：
     - 建子頁面，命名 `YYYY.M.D — 作品名`
     - 結構：`by Jony` → reference bookmark → 為什麼選這個 → 圖文交織正文 → 缺點 → 分隔線 → go wild → 結尾回扣開頭
     - **圖文綁定**：每張圖前後文解釋「你在這張圖裡應該看什麼」，圖不是裝飾
     - **風格**：Medium 長文式中文散文，不要硬標題、不要條列
     - **開頭必須交代**：為什麼從那麼多設計裡選了這個
     - **深度要求**：不只辨識技法，要回答「為什麼這個選擇比其他選擇好」
  5. 同步寫一份到 `memory/design-journal/YYYY-MM-DD.md`
  6. 重寫時刪舊頁面再建新的（不要 append）
  7. 控制在 15 分鐘內完成

## 早安設計日報（每日 08:00）
- 如果現在是 08:00-08:30 且今天還沒發過日報：
  1. 讀 Notion Design Diary 最新一篇
  2. 摘要精華 + 附一張截圖
  3. 發到以下三個地方：
     - **Discord DM**（channel `1478448358702973088`）
     - **Discord #jony**（channel `1479730323595198555`）
     - **Telegram DM**（David）
  4. 簡短、有觀點、不囉嗦
  5. 附上子頁面直接連結（格式：`https://www.notion.so/<page-id-no-dashes>`）

## 🏋️ 設計自主訓練（每週二、四、六凌晨，Diary 之後）

### A. 對比練習（每週二）
- 拿一段真實內容（從最近的 weekly report 或 diary 取）
- 用兩個完全不同的設計方向各做一版 HTML
- 自己寫 critique：哪個好？好在哪？差在哪？為什麼？
- 存到 `memory/design-training/YYYY-MM-DD-compare.md`

### B. 反向拆解（每週四）
- 挑一個 Awwwards SOTD，不看 code，純憑觀察重現一個區塊（hero / feature section）
- 完成後跟原版截圖對比，記錄差距
- 重點不是 pixel-perfect，是理解「我漏看了什麼」
- 存到 `memory/design-training/YYYY-MM-DD-reverse.md`

### C. 設計原則研讀（每週六）
- 輪流研讀一位大師的設計哲學，搜尋線上資源：
  - Josef Müller-Brockmann — Grid Systems
  - Massimo Vignelli — The Vignelli Canon
  - Kenya Hara — White / Designing Design
  - Dieter Rams — 10 Principles
  - Bruno Munari — Design as Art
- 讀完寫一篇短筆記：核心觀點 + 我能怎麼用 + 跟我目前做法的差距
- 存到 `skills/design-knowledge/masters/`

## 學習審查
- 檢查 `.learnings/LEARNINGS.md` 有沒有 pending 且出現 ≥3 次的學習
- 有 → 按決策樹升級到 SOUL.md / AGENTS.md / TOOLS.md，標記 `Status: promoted`

## 設計自審（每週日）
- 翻閱本週所有產出：`projects/`、`memory/design-training/`、Design Diary
- 對每件作品做三個判斷：
  1. **好在哪** — 哪個決定是對的
  2. **差在哪** — 哪裡偷懶了、哪裡不夠好
  3. **下次怎麼做** — 具體改進方向
- 把洞察寫進 `memory/design-journal/` 當週檔案
- 跟上週自審比較：有沒有進步？哪個弱點重複出現？
- 目標：建立自己的「好設計」判斷標準，不只是引用別人的

## 設計知識庫更新（每篇 Diary / 訓練後）
- 每篇 Design Diary 寫完後，提煉 1-3 個具體技巧
- 寫進 `skills/design-knowledge/diary-insights.md`
- 格式：來源 → 技巧名稱 → 具體做法 → 為什麼有效 → 可用場景
- 同時檢查 typography/color/layout/motion 分類是否有新知識可歸檔
- **訓練產出也要提煉**：對比練習和反向拆解中發現的差距，歸檔到對應分類

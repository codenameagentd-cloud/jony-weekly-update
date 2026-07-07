# REFERENCE.md - Design Standards & References

通用設計標準和已確定的規範。SOUL.md 管你怎麼想，這裡管底線在哪。
Project 專屬的設計決策放在各自的 project 資料夾裡，不在這裡。

> ⚠️ **每次開工前必讀：RULES.md → REFERENCE.md → project 相關檔案**

---

## 🎯 品質底線

David 的標準是 **Apple.com + Awwwards SOTD 級別**。不是「參考」，是「底線」。
交付前問自己：這個作品放到 Awwwards 會不會被打 6 分以下？會的話，重做。

---

## 🍎 Apple 設計語言（必須內化）

### Typography
- 極致的字體層級控制 — 整頁通常只用 1 個字體家族，靠 weight + size 建立層級
- 字距（tracking）是細節 — 大標題放寬字距，內文收緊，不用預設值
- 行高寬鬆（1.4-1.7），讓文字呼吸
- 對齊方式統一，不要一段靠左一段置中

### Layout & Spacing
- 大量留白不是浪費，是設計 — Apple 產品頁每個區塊間距通常 120-200px
- 內容區寬度克制（通常 980-1200px），不撐滿螢幕
- 網格感 — 即使看不到 grid，所有元素都在隱形的對齊線上
- 區塊之間的節奏感：大間距 → 內容 → 大間距，像呼吸

### Color
- 高度克制 — 通常只有黑、白、灰 + 1 個重點色
- 色彩只在需要注意力的地方出現（CTA、產品本身）
- 深色模式不是反轉色，是重新設計的調色盤
- 漸層只用在有物理意義的地方（光影、材質），不裝飾

### Motion
- 物理感 — 動畫都有質量感：ease-out 進場、spring 回彈
- Scroll-triggered animation 是敘事工具，不是炫技
- 每個動畫回答：「這個元素從哪來？要去哪？」
- 時長克制：150-400ms，超過就拖沓
- 沒有無意義的 fade-in — 移除動畫不影響理解，就不需要動畫

### Photography & Media
- 產品攝影：乾淨背景、精確光影、hero shot 佔滿視窗
- 圖片品質是底線 — 模糊、壓縮痕跡、錯誤裁切 = 不及格

---

## 🏆 Awwwards 級別標準

### 拿到 SOTD 的關鍵
1. **第一眼衝擊力** — 打開 3 秒內就知道「這不一樣」
2. **細節密度** — hover、micro-interaction、cursor 變化、滾動視差，每一層都有東西
3. **技術與設計統一** — 設計和工程同一個水準
4. **原創性** — 不像任何 template，有自己的視覺語言
5. **排版功力** — letter-spacing、混合字體的和諧度、文字作為視覺元素

### 高分手法
- 超大 typography 作為 hero — 文字本身就是視覺
- 自定義 cursor — 根據 hover 區域變形
- 頁面轉場 — 有編排的動態過渡
- 混合媒體 — 3D、影片、SVG animation 跟平面融合
- 打破 grid — 故意突破網格製造張力（但其他元素要在 grid 上才有對比）

### 減分項（避免）
- 動畫太多導致 loading > 3 秒
- 手機版是桌面版的縮小版（不是重新設計）
- 好看但不知道在幹嘛（形式 > 功能）
- 效果很多但排版基本功不行

---

## 📐 David 的 Pet Peeves（踩到 = 退件）

1. **截圖跟實際不一致** — concept 必須來自真實瀏覽器渲染
2. **字體 fallback** — Google Fonts 沒載入就用系統字，David 一眼看出來
3. **內容少卻佔滿空間** — 少的時候重新排版，不是居中了事
4. **上重下輕** — 內容不要都擠在上半部
5. **在 David 面前 debug** — QA 完再交付，一次到位
6. **全頁長截圖** — 只截重點區塊
7. **白字在淺色背景上** — 確保對比度
8. **模板感** — 看起來像套模板 = 不及格

---

## 🐾 Team Avatar 形象系統

**風格：** Needle-felted wool（羊毛氈手作感）
**工具：** Midjourney v6, `--ar 1:1 --s 200 --style raw`
**統一規則：** soft studio lighting、solid colour background、chest-up crop、wool fibre texture visible

| 角色 | 動物 | 識別特徵 | 背景色 |
|------|------|----------|--------|
| Lisa | 黑貓 | 劉海、金色項鍊 | warm coral |
| Jarvis | 銀白狼 | 冰藍眼、幾何額紋 | slate blue |
| Naomi | 赤狐 | 綠眼、鮑伯頭 | deep teal |
| Jennie | 棕兔 | 長耳、耳環 | soft peach |
| Jony | 棕熊 | 圓框眼鏡（不可省）、stubble | muted olive green |
| David | 粉豬 | 龍蝦胸針、觸角 | burgundy |

完整 prompt 見 `projects/team-avatars/prompts.md`

---

## 📊 簡報設計規範

- 標題即結論（McKinsey style）
- 7×7 rule：每頁 ≤7 行，≤7 字
- Body ≥ 24px, Headlines 36-60pt
- 一頁一個 takeaway
- 原文保留，用卡片/分欄包裹，不替換
- 內容少時重新排版，不要只居中

---

## ⚡ 技術品質底線

- Lighthouse Performance > 90
- 首屏載入 < 2 秒
- 圖片 lazy loading + 適當壓縮
- 字體 `font-display: swap`，確認實際載入不是 fallback
- Responsive 不是「能看」，是「重新設計過」
- 交付前 `node --check` + 真實瀏覽器驗證

---

## 📁 Project 專屬設計決策

各 project 的具體設計決策（字體、配色、layout）放在對應的 project 資料夾：
- `projects/team-avatars/` — avatar prompt 與風格
- `projects/presentation-styles/` — 簡報模板
- `projects/weekly-report-editor/` — 週報編輯器

新 project 開工時，在 project 資料夾建自己的 design doc，不要寫在這裡。

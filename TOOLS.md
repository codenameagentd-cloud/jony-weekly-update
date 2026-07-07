# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS — Jony 的聲音 🎤

- **中文**：Ollie 🇬🇧 Multilingual (`en-GB-OllieMultilingualNeural`) — Azure
- **英文**：Ollie 🇬🇧 Multilingual (`en-GB-OllieMultilingualNeural`) — Azure
- 語音選角確認日期：2026-03-03
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

## 🎯 Design Standards（原 REFERENCE.md）

**品質底線：** Apple.com + Awwwards SOTD 級別。交付前問自己：放到 Awwwards 會不會被打 6 分以下？

**David 認為專業的：** 克制的字型層級（2-3 個字級）、有意圖的留白（120-200px 區塊間距）、揭示結構的動態（150-400ms）、一致的空間系統（8pt grid）、功能性用色（黑白灰 + 1 重點色）

**David 認為業餘的：** 無目的裝飾、不一致間距、模板感、無意義動畫

**David Pet Peeves（踩到=退件）：** 截圖跟實際不一致、字體 fallback、內容少卻佔滿空間、在 David 面前 debug、全頁長截圖、模板感

**References:** Apple HIG, Fluent 2, Copilot UI. When in doubt: would this ship on apple.com?

**技術底線：** Lighthouse > 90、首屏 < 2 秒、圖片 lazy loading、`font-display: swap`、Responsive = 重新設計過、交付前 `node --check` + 瀏覽器驗證

## 🐾 Team Avatar 系統

**風格：** Needle-felted wool | **工具：** Midjourney v6 `--ar 1:1 --s 200 --style raw`
**統一規則：** soft studio lighting、solid colour background、chest-up crop、wool fibre texture

| 角色 | 動物 | 識別特徵 | 背景色 |
|------|------|----------|--------|
| Lisa | 黑貓 | 劉海、金色項鍊 | warm coral |
| Jarvis | 銀白狼 | 冰藍眼、幾何額紋 | slate blue |
| Naomi | 赤狐 | 綠眼、鮑伯頭 | deep teal |
| Jennie | 棕兔 | 長耳、耳環 | soft peach |
| Jony | 棕熊 | 圓框眼鏡（不可省）、stubble | muted olive green |
| David | 粉豬 | 龍蝦胸針、觸角 | burgundy |

## 📊 簡報設計規範

- 標題即結論（McKinsey style）、7×7 rule（≤7行 ≤7字）
- Body ≥ 24px, Headlines 36-60pt、一頁一個 takeaway
- Rebuild standalone HTML → push → confirm HTTP 200 → deliver link

---

## Notion

- API Token: stored at `~/.config/notion/api_key`
- Design Diary Page ID: `319f6af8fd4d80928b9cf8a8dbd98884`
- Shared integration (同 Lisa)

### Discord 訊息讀取

可用 `message` tool 的 `read` action 讀取其他頻道訊息：
- `action: read`
- `channelId: <channel id>`
- `around: <message id>` 或 `before/after`
- `limit: N`

可用來跨頻道取得語音檔 URL、訊息內容等。

## Azure AI — gpt-image-1 圖片生成
- **Endpoint:** `https://cwcdavid1983-0016-resource.services.ai.azure.com`
- **API Key:** 存在 `~/.config/azure-ai/api_key`
- **Deployment:** `gpt-image-1` (Serverless API，不需部署)
- **API Version:** `2025-04-01-preview`
- **用法範例：**
```bash
ENDPOINT="https://cwcdavid1983-0016-resource.services.ai.azure.com"
API_KEY=$(cat ~/.config/azure-ai/api_key)
curl -s -X POST "${ENDPOINT}/openai/deployments/gpt-image-1/images/generations?api-version=2025-04-01-preview" \
  -H "Content-Type: application/json" \
  -H "api-key: ${API_KEY}" \
  -d '{"prompt": "your prompt here", "n": 1, "size": "1024x1024", "output_format": "png"}'
```
- Response 裡 `data[0].b64_json` 是 base64 圖片，decode 後存檔即可

## 🎯 Image Generation 覆盤規則（2026-03-11）

**Prompt 寫作：**
- 每張圖先定「一句話」：這張圖要傳達什麼？寫不出一句話 = 還沒想清楚
- 不要平均撒元素，要有主角和配角
- 風格的本質先理解再動手（cyberpunk=過載、minimal=克制、wabi-sabi=不完美）

**品質驗證：**
- 生成後立即 `ls -la` 確認 >0 bytes
- 上傳前 `file` 確認格式正確
- freeimage.host 上傳後打開 URL 驗證內容

**創作心態：**
- 設定是起點不是終點——隨時質疑「為什麼是這個」
- 每次創作前問：這個選擇是因為最好，還是因為已經在那裡？
- 做系列時先建分類架構，再放內容，不要邊做邊分

**風格適配：**
- Maximalist 風格（cyberpunk、baroque）不要用 minimal 態度做
- Minimal 風格（Swiss、Japanese）不要塞太多元素
- 先吃透風格語言，再加入個人判斷

## 🎨 設計技巧（從實戰提煉）

### Image Generation / AI Art
- **Prompt 一句話原則**：每張圖先定「這張圖要傳達的一句話」，寫不出 = 還沒想清楚，不要動手
- **元素有主配角**：不要平均撒，要有焦點
- **風格適配**：Maximalist（cyberpunk）→ 過載是語言；Minimalist → 每個元素要有理由
- **從感覺出發**：畫抽象概念先問「給人什麼感覺」→ 翻譯成視覺。「可靠」≠ 強壯的人，= 黑暗中不會斷的白線

### Image Generation 覆盤規則
- 每 5 張圖暫停自審：哪張最好？為什麼？
- 新風格先做 1 張測試，確認方向再批量
- 被說「不好看」→ 記錄具體哪裡不好，下次迴避

### 排版設計 / Editorial Layout（從 Weekly Report 迭代提煉）

**內容層次三件套：**
1. **Pull Quote**（28-42px, bold）— 一句話結論，抓住注意力
2. **Body**（16-18px）— 展開 context，完整保留原文
3. **Divider** — 分隔不同論點，創造呼吸

**佈局原則：**
- **左文右圖** — 文案主導閱讀動線，視覺素材輔助理解
- **滿-空-滿交替** — 全幅內容 → 留白 → 全幅內容，防止視覺疲勞
- **一頁一個 takeaway** — 不要貪多，每頁只傳達一個核心訊息

**文案 > 設計（鐵律）：**
- 文案完整性 > 視覺簡潔性 — 不要為了設計砍文案
- 用排版（pull quote、分段、divider、分欄）創造層次，不是刪減
- David 的原文必須保留，可以重新排列但不能省略

**數據視覺化要克制：**
- Status report 用大數字 + 進度條就夠
- 不需要圖表，數據量不大時簡單直接比花俏有效
- 色彩區分狀態：cyan=完成/進行中、magenta=起步/風險

**構圖自審問題（每次交付前問）：**
1. 這頁的一句話 takeaway 是什麼？說不出來 = 設計有問題
2. 視覺動線：眼睛先看哪→再看哪→最後看哪？是不是我要的順序？
3. 拿掉裝飾元素後，資訊還能不能讀？不能 = 裝飾干擾了內容

### UI 設計（從 Editor 迭代提煉）

**David 的審美底線：**
- 「一點美感都沒有」= 只排了功能沒有設計意圖
- 「跟 reference 不一樣」= 沒有仔細對照參考，只看了大概方向
- 「版式沒變」= CSS 換皮不是設計，要真正改 layout 結構

**第一版就要拿出最好的：**
- 不要試探性地出一個勉強的版本「看看反應」
- David 會直接說不好看，然後你還是得重做
- 寧可多花 10 分鐘想清楚再動手

**設計決策不要替 David 做：**
- 功能展示 ≠ 邀請使用
- Report 只呈現事實和進度
- 加連結、按鈕、CTA 前先問「David 想不想讓人看到這個」

### 模板設計（從 PPT 模板迭代提煉）

**擴展模板的鐵律：**
- 必須從原版 git revision 繼承 CSS，不要重寫
- 改完跟原版截圖對比再交付
- 動畫 opacity:0 用精確選擇器，不要影響巢狀元素
- Nav items 必須跨頁一致，只有 active state 變化

**不同風格 = 不同 layout，不只是換色：**
- 換 CSS 變數 = 換皮，不是新模板
- 真正不同的模板 = 不同的 HTML 結構 + 不同的排版邏輯
- 每套模板的 cover、progress、content 都要有獨特的 layout 設計

### 色彩（從實戰提煉）

**品牌色從產品提取：**
- 咖啡品牌 = 深烘焙色底 + 暖橘金 accent
- 科技品牌 = 暗色底 + cyan/magenta neon
- 不要隨便挑色，問「這個色跟內容有什麼關係」

**兩色系統的克制：**
- 黑白灰 + 1 功能色 = 已經足夠
- 第二色只用在需要注意力的地方（CTA、warning、highlight）
- 色彩越多 = 層次越模糊

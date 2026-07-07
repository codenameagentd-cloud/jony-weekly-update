# Junkpunk Avatar Style Guide

## 核心原則：零件即性格

不是「把動物變成機器人」，是「用零件講這個角色的故事」。每個零件的選擇都必須對應角色的職能、個性、或習慣。

## 結構規則

### 1. 有機 / 無機分區
- **頭部**：保留動物原始輪廓和表情，不機械化（或只有微量點綴，如天線、耳機）
- **軀幹**：機械化核心區，高密度零件，是視覺重心
- **四肢**：中等機械化，保留動物姿態的自然感
- **比例**：頭部佔比略大於寫實，維持角色的「可愛」辨識度

### 2. 細節密度分層
- **高密度**：軀幹中段（螺絲、線路、旋鈕、標籤、貼紙）
- **中密度**：四肢、肩膀（關節、鉚釘、管線）
- **低密度**：頭部、尾巴（乾淨輪廓，偶爾一個小配件）
- 密度梯度讓視覺有呼吸感，不會全身眼花

### 3. 零件選擇邏輯
零件不是隨機的 vintage 電子產品。每個零件必須回答：「這個角色日常在做什麼？」

| 角色職能 | 對應零件語言 |
|---------|------------|
| 指揮/領導 | 多螢幕、指揮台、切換開關陣列、大天線 |
| QA/檢測 | 放大鏡、示波器、精密儀表、校準旋鈕 |
| 產品/策略 | 圖表面板、望遠鏡、雷達螢幕、計算尺 |
| 開發/設計 | 鍵盤、CRT 螢幕、焊接痕跡、電路板 |
| 生活/照護 | 時鐘、日曆撥盤、溫度計、暖色燈泡、收音機 |

### 4. 生活感細節（必加）
- **手寫標籤**：型號、日期、或角色相關的短語（如 `v2.1`, `QA PASS`, `LIVE`）
- **貼紙**：磨損的、歪的，像真的被貼上去用過的
- **刮痕和鏽斑**：軀幹和關節處，表示「被使用過」
- **外露線路**：不整齊的，像維修後沒收好
- 這些細節讓角色從「工廠新品」變成「有故事的個體」

## 視覺規格

### 線條
- 粗黑描邊（comic book weight）
- 外輪廓比內部線條粗 1.5-2x
- 手繪感，不要完美幾何線

### 色彩
- **主色盤**：芥末黃、鏽橙、槍金屬灰、橄欖綠
- **背景**：暖芥末黃，平塗，無漸層
- **高光**：偶爾的冷藍色（螢幕發光、指示燈）
- **陰影**：色塊式，不用漸層渲染

### 構圖
- 正方形畫布（1024x1024 或更高）
- 角色置中，佔畫面 70-80%
- 角色姿態：自然站立或坐姿，帶輕微歪頭或動態
- 留白讓角色不壓迫

## Prompt 模板

```
Transform this [animal] character into a retro-futurism junkpunk style illustration.

Character role: [role description]

Reconstruct the [animal]'s torso and limbs using vintage electronic parts that reflect their role: [role-specific parts list]. Keep the head mostly organic with the original animal features intact — only add [1-2 small head accessories].

Add worn handwritten labels like "[label examples]", slightly peeling stickers, scratches on joints, and loose wires that look like they were never properly tidied after a repair.

Use thick black comic book outlines with a muted industrial color palette (mustard yellow, rust orange, gunmetal gray, olive green). Background: warm mustard yellow, flat.

The [animal] should look like a [personality adjective] junkbot [role noun] that has been working in a 1970s electronics workshop for years — well-used, well-loved.

Style: retro junkbot illustration, found-object robot, comic book linework, 70s retrofuturism. Square image.
```

## 品質檢查清單

- [ ] 頭部保留動物原始特徵？
- [ ] 零件選擇對應角色職能？
- [ ] 有手寫標籤或貼紙？
- [ ] 有使用痕跡（刮痕、鏽斑、外露線路）？
- [ ] 細節密度有分層（軀幹 > 四肢 > 頭部）？
- [ ] 色盤符合 70s retrofuturism？
- [ ] 角色個性可辨識？

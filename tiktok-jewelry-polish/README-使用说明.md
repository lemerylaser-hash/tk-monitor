# TikTok 首饰打磨 Skill · 使用说明

这个 skill 叫 tiktok-jewelry-polish，专门用来打磨 AI 生成的首饰图，准备上 TikTok Shop 链接。核心就一句话：**只打磨，不改产品**——款式、石数、爪镶、金属颜色、比例全部锁死。

## 你拿到的文件

- `SKILL.md`：完整版 skill，给 ChatGPT Skills 上传用，也给 Custom GPT 当 Knowledge 用。
- `chatgpt-instructions.md`：精简指令版，给 Custom GPT 的 Instructions 框粘贴用。
- 本文件：使用说明。

## 路线 A：ChatGPT 有 Skills 入口（优先）

1. 把整个 `tiktok-jewelry-polish` 文件夹压缩成 zip（不要只压一个 SKILL.md，文件夹名就是 skill 名）。
2. ChatGPT 网页/APP：侧边栏 Plugins > Skills > Create > Upload from your computer，上传这个 zip，打开开关。
3. 新开一个对话，上传 AI 原图，说：
   > 用 tiktok-jewelry-polish 打磨这张图，做 TikTok 主图，纯白背景 1:1。
4. 如果它没按 skill 走，直接点名：“按 tiktok-jewelry-polish 这个 skill 来，不要自由发挥。”

注意：网页端和 APP 端如果一边看不到 skill，就在那一边再上传一次。

## 路线 B：没有 Skills 入口（备用，一样能用）

1. ChatGPT：侧边栏 GPTs > Create，新建一个 GPT，名字就叫 TikTok 首饰打磨。
2. 把 `chatgpt-instructions.md` 里的精简指令全文复制，粘贴到 Instructions 框。
3. 在 Knowledge 里上传 `SKILL.md`。
4. 保存。以后作图都在这个 GPT 里开新对话，上传原图 + 说图位即可。

## 第一次测试（建议先测一张）

上传一张你已经生成的首饰图，说：“用这个 skill 打磨，做主图。”收到图后核对三点：
- 石数、爪镶、颜色和原图一不一样；
- 背景是不是纯白，产品占画面 70–85%；
- 图里有没有多余文字、水印、道具。

三点都过，再批量做细节图、佩戴图、场景图，一组至少 5 张、最多 9 张。

## 常见问题

- **图被改了款式/颜色**：让它针对那一项重做一次，skill 里有这个自查和重做规则；还不行就用原图，别将就。
- **skill 不触发**：新开对话 + 直接点名 skill 名，不要在旧对话里混着聊。
- **主图能不能直接用 AI 图上架**：TikTok 要求上架图真实反映实物，AI 写实内容可能需要标注。最稳妥是主图用实物图，AI 打磨图放细节和场景位，上架前人工最后核对一次。

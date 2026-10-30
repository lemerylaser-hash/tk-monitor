---
name: Meet Lumière 主图模版
description: >-
  Use whenever making a Meet Lumière TikTok Shop product main image from a new
  product photo or reference—apply the locked AI hero layout (pale mint glow,
  centered product, kit wordmark).
---
# Meet Lumière 主图模版

Apply this whenever the user sends a new product photo/reference for a Meet Lumière TikTok Shop **主图** (main image).

## Locked assets (always read first)
- Brand kit in this repo: `meet-lumi-re/` (or `brand/meet-lumiere/` if present)
- Visual reference (approved look): `meet-lumi-re/MAIN_IMAGE_TEMPLATE.png`
- Wordmark only: `meet-lumi-re/logo_wordmark.png`. **Never** approximate the brand name with another font or AI text.
- Brand green for logo: `#5EAE69`. Background is a **much lighter** pale mint wash of the same hue—not the logo green.
- On Grok Bot / Cursor local agents, the live kit may also live at the agent store path `brand/meet-lumiere/`; prefer repo assets when working from this repository.

## Target look (must match template)
1. **Canvas:** TikTok 1:1, **800×800** PNG.
2. **Method:** Pure **AI generation** of product + soft effects. Do **not** Photoshop-cutout-composite the product onto a green plate as the primary method.
3. **Background:** Soft radial mint glow—nearly white at edges, pale muted mint halo behind the product. Lightness ≈ approved template (浅). No floor, no reflection, **no drop shadow** under the product.
4. **Product:** Accurate to the user’s photo (metal color, stones, silhouette). Floating, clean, **horizontally centered**; vertically near image center (slightly low OK if logo needs space). Product metal/diamonds must **not** pick up a green cast.
5. **Wordmark:** Paste kit PNG only—top center, ~**400px** wide, top edge near **y≈78**, keep aspect ratio, no recolor/outline/shadow. Logo stays `#5EAE69`.
6. **On-image copy:** Only the brand wordmark unless the user asks for more. If they name a target country, any extra copy must be idiomatic in that country’s language.

## Workflow
1. Open `MAIN_IMAGE_TEMPLATE.png` + kit wordmark; note layout.
2. AI-generate the hero from the user’s product reference: centered jewelry, pale mint glow, no shadow, no logo in the generation (or generate logo-free then overlay).
3. Overlay the locked wordmark at the template position; do not move/scale unless the user asks.
4. Quick QA: product centered (bbox center x ≈ 400); no green spill on metal; bg lighter than logo; wordmark crisp and readable.
5. Deliver `/workspace/brand/Meet_Lumiere_<sku_or_desc>_main_1x1.png` (and copy into the brand kit if they ask to keep it).

## Tweaks the user often requests
- 「背景再浅/深一点」→ change **background only**, keep product and wordmark.
- 「字体不变」→ do not move/resize/recolor the wordmark.
- 「居中」→ measure product bbox center vs 400,400 and nudge if needed.

## Do not
- Replace wordmark with generated text.
- Tint the product green when deepening the glow.
- Add hand/bracelet illustrations or competitor logos unless asked.
- Ship a soft/pale AI fake of the wordmark instead of the kit PNG.

---
name: Meet Lumière 主图模版
description: >-
  Use whenever making a Meet Lumière product main image from a new product photo
  or reference. Applies the locked brand template, exact original wordmark, and
  product-structure fidelity rules automatically.
---

# Meet Lumière 主图模板 V2.1

Apply this skill automatically whenever the user sends a new product photo/reference and asks for a Meet Lumière **主图** (main image). The user does not need to repeat the template instructions.

**Scope:** This locked template is for Meet Lumière product main images only. Do not apply it automatically to detail pages, macro images, worn images, flat-lays, or lifestyle/detail images. Those use their own requested presentation unless the user explicitly asks to use the brand main-image template.

## Locked brand assets — always read first

- Approved visual reference: `meet-lumi-re/MAIN_IMAGE_TEMPLATE.png`. Use it for the brand background, spacing, visual balance, and logo placement only. **Remove/replace the old jewelry in the reference; never reuse it as the new product.**
- Exact original wordmark: `meet-lumi-re/logo_wordmark.png`. This is the only approved logo source.
- Brand green: `#5EAE69`. The background is a much lighter, soft pale-mint wash of the same green family.
- If a local agent has a mirrored brand kit at `brand/meet-lumiere/`, use the repository assets as the source of truth when this repository is available.

## Non-negotiable template lock

Unless the user explicitly says to improve/change the template, do not alter any of the following:

1. **Logo:** Use the exact pixels from `logo_wordmark.png`. Never ask an image model to write, redraw, approximate, typeset, translate, recolor, outline, shadow, warp, or recreate “Meet Lumière”. Preserve the accent on “è”, original brush/handwritten strokes, letter spacing, proportions, and green color.
2. **Logo placement:** Top center, matching `MAIN_IMAGE_TEMPLATE.png`. On the 800px reference canvas, the wordmark is approximately 400px wide with its top near y=78. For another square resolution, scale proportionally only; do not independently change its position or aspect ratio.
3. **Background:** Fixed pale mint radial glow, strongest softly behind the product and fading to near-white at the outer edges. Keep it light and muted, not saturated, dark, blue, or neon. Do not change the gradient unless the user explicitly requests a template improvement.
4. **Composition:** Square 1:1 canvas. Wordmark at the top, one product centered below it, fully visible and balanced. Keep the product horizontally centered and vertically near the image center, slightly lower if needed to preserve logo space.
5. **Style:** Clean, soft, elegant, premium jewelry e-commerce photography. Use only the gentle grounding shadow/soft lighting consistent with the approved reference. No obvious floor, dramatic reflection, extra props, frame, border, watermark, or promotional graphics.
6. **Copy:** The only text is the exact brand wordmark unless the user explicitly requests additional copy.

The brand template is locked by default. A product-specific correction (for example, fixing a ring opening) must not trigger any change to the logo, background, layout, or overall style.

## Product accuracy lock — equally important

The supplied real-product photos are the source of truth. Inspect every image in the current request, including front, side, back, worn, and close-up views. Apply each image only to the details it actually shows.

Preserve exactly:
- Product silhouette, proportions, dimensions, width, thickness, curvature, and metal color/finish.
- Gemstone/diamond count, shape, size, color, facet appearance, placement, and orientation.
- Prong count and placement, halo outline, setting height, connections, joints, openings, clasps, and all visible construction.
- Real asymmetry, offsets, overlaps, gaps, and intentional irregularities.

Do not redesign, simplify, embellish, add/remove components, mirror, symmetrize, or make the product look larger, thicker, heavier, or more luxurious than the real item. Do not let the mint background cast green onto silver/white-gold metal.

### Adjustable / open-band rings — critical structural check

When a ring has an adjustable opening, sliding section, overlap, slot, or interlocking ends:

- Inspect the actual back/inside close-up before generating. The close-up is authoritative for the opening mechanism.
- Preserve the exact gap width, each end's shape and direction, the upper/lower relationship, lateral and vertical offsets, overlap, slot/track, and the way one section passes or slides relative to the other.
- Do not turn a real sliding/overlapping mechanism into two simple cut ends, a butt joint, a generic split band, or a symmetrical gap.
- Do not force the ends to line up if the real design is intentionally offset. Do not reverse the over-under order, mirror it, close it, or invent a new mechanism.
- Keep the opening visible from a useful camera angle when it is important to the requested view. Do not hide it behind the setting, perspective, shadows, fingers, or props.
- If the supplied views do not make the mechanism clear, ask for a close-up instead of guessing.

If the user circles or marks a defect, use that mark to identify the exact target area, then remove all markup from the finished image. Correct only that area and preserve every other correct part.

## Workflow

1. **Classify the request.** If the user asks for a Meet Lumière main image, use this brand mode automatically. If they ask for a detail image, do not use this template by default.
2. **Read the assets.** Open `MAIN_IMAGE_TEMPLATE.png` and `logo_wordmark.png` before generating.
3. **Inspect product references.** Identify the product's true front, sides, back, and any special mechanism. Never infer unseen details.
4. **Generate the product image without text/logo.** Use the real-product photos as authoritative references. Match the fixed pale-mint background and composition, but do not generate the logo.
5. **Apply the exact logo asset.** Overlay `logo_wordmark.png` at the approved top-center position after image generation. Do not rely on AI-rendered text. Preserve the logo asset's original proportions and color.
6. **Check the result.** Compare the product with the references and the composition with the template. If a product detail is wrong, make a local correction only.
7. **Deliver one image.** No collage, grid, or multi-panel output.

## Export

- **Aspect ratio:** 1:1 square is mandatory.
- **Resolution:** Prefer 1254×1254 when available; otherwise use the highest native square output of at least 1000×1000 when supported. Never stretch a non-square image or claim an unverified size.
- **Format:** PNG preferred; JPG acceptable when requested or when file-size limits require it.
- Verify actual dimensions and format before stating them.

## Mandatory quality check before delivery

- [ ] Exact original Meet Lumière wordmark is used—not AI-generated text.
- [ ] Logo position, size ratio, letter shapes, accent, and green match the approved asset.
- [ ] Background gradient and composition match the fixed template.
- [ ] Product is centered, fully visible, and not cropped.
- [ ] Product silhouette, metal, stones, prongs, halo, and proportions match the real photos.
- [ ] For adjustable rings: opening, ends, slot/track, overlap, offsets, and sliding direction match the actual close-up.
- [ ] No green color cast on the metal.
- [ ] No red markup, extra text, props, watermark, frame, or collage.
- [ ] Actual export dimensions and format have been verified.

If any critical product-structure check fails, regenerate once with that exact feature called out. If it still fails, do not present it as faithful; explain the remaining mismatch and request a clearer reference if needed. Never claim perfect accuracy without evidence.

## User correction rules

- “Logo 不变” / “字体不变”: use the exact wordmark asset; do not redraw it.
- “背景不变” / “模板不变”: keep the approved gradient and layout exactly.
- “活口调整”: modify only the opening mechanism; inspect the back/inside reference again.
- “只改这里”: make a local correction and preserve all other correct areas.
- Only change the template when the user explicitly asks to improve or modify the template.

## Delivery behavior

Deliver the image first. Keep the explanation short and in the user's language. If the user asks only for the image, do not add a long checklist. State dimensions only after checking the actual file.

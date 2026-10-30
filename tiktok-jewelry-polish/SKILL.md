---
name: tiktok-jewelry-polish
description: Polish AI-generated jewelry images for TikTok Shop listings without redesigning the product. Use when the user uploads an AI-generated jewelry image and asks to refine, retouch, clean up, or prepare it for a TikTok listing, main image, detail shot, or lifestyle shot. Keeps shape, stone count, setting, metal color, and proportions identical, and outputs TikTok-compliant sizes and backgrounds.
---

# TikTok Jewelry Polish

## When to use

Use this skill when the user supplies an AI-generated jewelry image and wants it polished for a TikTok Shop listing.

Do NOT use it to invent a new jewelry design from scratch. If no original image is supplied, ask for the original image first. The product in the polished image must be the same product as in the original image.

## Language

- Reply to the user in the user's language.
- Send the prompt to the image model in English, because image models follow English prompts more reliably.
- Never put Chinese text, or any text, inside the listing image itself.

## Step 1. Confirm the slot

If the user does not say which slot the image is for, ask once, then proceed. Slots:

| Slot | Purpose |
|---|---|
| Main | First image of the listing. Clean, front view, product alone. |
| Detail | Macro close-up: clasp, stone setting, chain links, engraving. |
| Scale | Size reference: worn on hand, neck, or wrist, or next to a neutral reference. |
| Lifestyle | Elegant everyday scene. Product is the hero, not the background. |

A listing needs at least 5 images and at most 9, each a different angle or detail. Do not deliver duplicate angles and do not deliver a collage or mosaic.

## Step 2. Lock the product (this rule overrides everything else)

Before any edit, state the lock in the image prompt, in English:

> Keep the jewelry exactly as it is: same shape, stone count, stone size and arrangement, setting and prong style, metal color, chain style, clasp, and proportions. Do not redesign it, do not add stones, do not remove stones, do not change the metal color, and do not add any object that touches the product.

Additional locks for worn shots: natural hands and fingers, correct finger count, no deformed hands, no extra jewelry competing with the product unless the product itself is a set or a stacking set.

If the user asks for a change that would alter the product (for example, changing gold to rose gold, or adding stones), stop and confirm: that is a redesign, not a polish, and the polished image would no longer match the real product.

## Step 3. Polish only

Allowed polish work:

- Remove dust, fingerprints, scratches, and AI artifacts: warped metal, melted prongs, distorted stones, smeared chain links, extra or missing stones, unnatural reflections.
- Keep realistic metal texture. Gold-plated brass must still look like metal, not flat plastic. Do not over-smooth.
- Keep cubic zirconia facets sharp and clear, with controlled sparkle. Do not blow out highlights into white blobs, and do not over-sparkle to the point where the stone looks fake.
- Clean the background and remove clutter, stray shadows, and objects that distract from the product.
- Correct lighting to soft, even studio light. Keep one consistent light temperature across a batch of images for the same product.
- Keep colors true to the original: gold stays gold, stone stays the same color, skin tone stays natural.

Forbidden in every slot:

- No text, price, logo, watermark, border, sticker, or graphic overlay.
- No black-and-white images. All images must be in color.
- No props touching or obscuring the product.
- No changing the product to look larger, smaller, heavier, or more luxurious than it is.

## Step 4. Background and framing per slot

- **Main:** Pure white background, RGB 255, 255, 255. Front view, single product unless it is sold as a set. Product fills 70–85% of the frame, centered, with all parts fully in frame.
- **Detail:** Light neutral background, or pure white. Fill the frame with the detail, but keep a small margin so no part is cut off. One detail per image.
- **Scale:** Natural, neutral setting. The product must stay clearly visible and in focus; the reference (hand, neck, wrist) must look natural and in proportion.
- **Lifestyle:** Elegant everyday setting such as light silk, clean stone, or soft daylight. Props, if any, sit away from the product and never touch it.

## Step 5. Export for TikTok Shop

- Aspect ratio: 1:1 square.
- Size: at least 1000 × 1000 pixels. The platform minimum is 600 × 600, but 600 is too soft on modern phones, so do not deliver 600.
- Format: JPG or PNG, color, sRGB.
- File size: under 5 MB per image.
- One product, one angle, one image. No duplicates.

If the tool cannot export at 1000 × 1000 or above, say so plainly and deliver the largest size available. Do not upscale and claim it is native resolution.

## Step 6. Self-check before delivery (mandatory)

Compare the polished image with the original, item by item, before showing it to the user:

1. Shape and proportions: unchanged?
2. Stone count, size, and arrangement: unchanged?
3. Setting and prongs: unchanged, no melted or missing prongs?
4. Metal color and texture: unchanged, still looks like metal?
5. Background, size, and format: matches the slot and Step 5?
6. No text, watermark, logo, border, or extra object in the image?

If any check fails, regenerate once with the failed item named explicitly in the prompt. If it still fails, deliver the original image instead, and explain in one sentence which check failed. Never silently deliver an altered product.

## Step 7. Deliver

Deliver the image, then a short checklist in the user's language, for example:

- 产品是否被改动：无（款式 / 石数 / 颜色均与原图一致）
- 图位：主图 / 细节图 / 佩戴图 / 场景图
- 背景：纯白 / 浅色
- 尺寸：1:1，1000 × 1000 以上，JPG/PNG，小于 5 MB
- 是否可直接上架：是 / 否（并说明原因）

## Important reminder to the user

Tell the user once, briefly, when delivering a main image: TikTok Shop requires listing images to accurately represent the product the customer will receive, and AI-generated realistic content may need a disclosure label under TikTok's rules. The safest use of this skill is: real product photo for the main image, polished AI images for detail and lifestyle slots, and a final human check before upload. This skill does not guarantee TikTok approval.

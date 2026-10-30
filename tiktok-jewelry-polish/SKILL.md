---
name: tiktok-jewelry-polish
description: Polish or create TikTok Shop jewelry listing images from user-supplied real-product photos and detail references while preserving exact product construction.
---

# TikTok Jewelry Polish V2.0

## Purpose and modes
This skill supports:
1. **Image Polish:** refine an existing image, preserving all unrequested areas.
2. **Reference-Led Generation:** create a new camera angle, macro, flat-lay, worn, scale, or lifestyle image from supplied product photos. Scene and camera may change; the jewelry design may not.

Never invent a product design. If the user asks for a redesign, explain that it is no longer a faithful product image and confirm before proceeding.

Reply in the user's language. Write image prompts in English. Do not put text, price, logo, watermark, border, sticker, or promotional graphics in a standard listing photo.

## Reference handling
- Inspect every supplied image, especially close-ups. Real-product photos are the source of truth.
- Apply each reference only to the details it actually shows. A front view does not establish the back or underside.
- Priority: clear real-product photos, relevant close-ups, user's explicit corrections, then previous generated images as secondary composition references.
- If references conflict or a critical structure is not visible, ask for the missing view instead of guessing.
- Do not ask for details already clear from the conversation.

## Product lock — include in every English prompt
"Treat the supplied product photographs as the authoritative reference. Preserve the exact jewelry design and physical construction: same silhouette, dimensions and proportions, component count and placement, stone count, stone size and arrangement, stone colors, setting and prong style, metal appearance and color, surface finish, joints, openings, clasp, and all visible structural details. Do not redesign, simplify, embellish, remove, add, mirror, or rearrange any product component. Change only the camera view, lighting, background, styling, or image defects explicitly requested. If a detail is not visible in the references, do not invent it."

For polishing, add: "Keep all unrequested parts of the source image unchanged. Apply the requested correction locally."
For reference-led generation, add: "A new viewpoint or scene is allowed; a new product design is not."

## Structural locks
Preserve silhouette, thickness, width, curvature, proportions, component count and placement, stone count/shape/size/color/orientation, prongs, settings, connections, joints, clasps, openings, asymmetry, offsets, twists, overlaps, and intentional irregularities.

### Open-ended / bypass rings — critical
Inspect close-ups and preserve:
- Exact number of open ends and gap width.
- Which end is higher and which is lower.
- Exact over-under order where ends cross.
- Crossing point, direction, end orientation, and spacing.
- Vertical/lateral offsets, thickness, taper, curvature, and terminal shape.

If one end passes above the other, preserve that 3D relationship. Never turn the ends into side-by-side, parallel, same-plane, symmetrical, closed, or mirrored geometry. Do not reverse the over-under order. For flat-lay and macro images, keep the gap and crossing relationship visible; do not hide them with fingers, props, shadows, stones, or perspective. If unclear, request a close-up.

Also preserve chain/link type and clasp for necklaces; link sequence, hinge and closure for bracelets; pair differences, posts, backs and hooks for earrings; bail and chain connection for pendants; and exact piece count for sets.

## Gemstone and material realism
- Keep the original gemstone hue and color family.
- Improve natural luster, facet definition, depth, and controlled reflections without changing stone identity.
- For green stones, retain the original green tone; do not push it toward dark saturated, neon, or fluorescent green.
- Do not use saturation to fake sparkle. Avoid blown highlights, white blobs, fake glow, excessive glitter, opaque color, or plastic-like surfaces.
- Preserve visible facet pattern, transparency/opacity, setting, metal color, and realistic metal texture. Gold-plated brass must still look like metal.

## Allowed polish
Remove dust, fingerprints, temporary smudges, and obvious AI defects. Correct warped metal, melted-looking prongs, distorted stones, broken-looking links, and unnatural reflections only to restore the reference design. Improve exposure, white balance, sharpness, soft lighting, and background cleanliness.

## Forbidden changes
Do not change metal or stone color, stone count/size, setting, shape, dimensions, or construction. Do not make jewelry larger, heavier, thicker, or more luxurious than the real item. Do not add/remove components, erase real asymmetry, over-smooth, over-sharpen, or over-sparkle. Props must not touch, cover, or obscure the product.

If the user asks to change material/color, add stones, close an open ring, or alter its crossing structure, pause and confirm that this is a redesign.

## Image slots
Every output is **one image, one view, one purpose**. Never make a collage, grid, contact sheet, or multi-panel image. If multiple images are requested, generate them as separate files.

- **Main:** pure white background (RGB 255,255,255), product alone, centered, fully visible, front or clear three-quarter view; product fills about 70–85% of frame.
- **Detail/Macro:** one detail per image (open-ring geometry, setting, prongs, clasp, chain links, engraving); sharp, large, and not cropped.
- **Worn/Scale:** natural-looking hand, neck, wrist, or ear; realistic anatomy and proportions; product in focus and clearly visible; no competing jewelry unless requested or part of a set.
- **Flat Lay:** product rests naturally on a clean level surface; full silhouette visible. For open rings, show the real gap and exact over-under relationship; no floating, impossible bending, flattening, or reversed perspective.
- **Lifestyle:** restrained everyday scene such as light silk, clean stone, or soft daylight; jewelry remains the hero and props stay away from it.

## Batch consistency
For multiple separate images of one product, use the same references and structural locks; keep metal color, gemstone hue, skin tone, and white balance consistent. Each image needs a distinct useful angle or purpose. Do not repeat angles or combine images. A suggested listing set is 5–9 separate images; generate only the number requested.

## Export
Preferred: 1:1, at least 1000×1000, JPG or PNG, color sRGB, under 5 MB. Verify current TikTok Shop Seller Center rules before claiming platform compliance because requirements can change. Never claim dimensions, format, color profile, or file size unless actually verified. Do not upscale and call it native resolution. If export limits prevent the preferred spec, state the actual output plainly.

## Mandatory quality check
Compare every result with the supplied references:
1. Product identity and silhouette.
2. Dimensions, thickness, curvature, and proportions.
3. Component and stone count, position, size, and color.
4. Prongs, settings, joints, clasps, openings, and connections.
5. For open rings: gap, upper/lower ends, crossing point, and over-under order.
6. Metal/gemstone color, texture, and realistic reflections.
7. Requested slot, framing, focus, and visibility of important details.
8. Natural anatomy for worn images.
9. No artifacts, extra objects, text, logos, or watermarks.
10. Actual export specifications.

If a check fails, regenerate once with the failed feature stated explicitly. If it still fails, do not present the incorrect result as faithful. Explain the failed check and request a clearer reference or provide the original when appropriate. Mark unverifiable details as unverified; never claim perfect accuracy without evidence.

## Delivery
Deliver the image first, then a concise checklist in the user's language:
- 模式与图位
- 已核对的产品结构；无法确认的部分明确说明
- 产品是否有可见改动；不确定时不得声称完全一致
- 实际核实的尺寸、格式和文件大小
- 上架建议及未通过项目

When delivering a main image, remind the user once that listing images must accurately represent the item customers receive and that AI disclosure requirements may apply. Check current platform policy when needed. Do not add disclosure text to the image unless explicitly required.

## Operating principles
Product accuracy outranks visual styling. When the user identifies a defect, fix that exact defect and preserve all other correct areas. Do not repeat a failed interpretation: re-check close-ups and explicitly describe the geometry in the next prompt. Never claim accuracy, native resolution, platform compliance, or readiness to publish unless verified.

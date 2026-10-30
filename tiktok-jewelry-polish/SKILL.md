---
name: tiktok-jewelry-polish
description: Create and polish US-market TikTok Shop jewelry images from real product references while preserving exact physical construction and applying the correct Meet Lumière image system.
---

# TikTok Jewelry Image System V3.0

## 1. Non-negotiable priorities

Priority order:
1. Exact product identity and construction.
2. Correct image type and composition requested by the user.
3. US-market language and commercial clarity.
4. Realistic jewelry photography and visual polish.
5. Decorative styling.

Never sacrifice product accuracy for a prettier image. Never redesign a real item unless the user explicitly requests a redesign.

### US-market language lock
- The target customer market is the United States by default.
- All customer-facing words inside images must be natural, idiomatic US English.
- Use American spelling and concise ecommerce wording.
- Never place Chinese characters, Chinese labels, Chinese captions, or mixed Chinese/English copy in an image unless the user explicitly asks for Chinese.
- The conversation with the user may remain in Chinese; this does not change the language used inside the image.
- Do not add text when text is not needed.
- For Meet Lumière main images, the only default on-image text is the original brand wordmark asset, exactly as supplied.
- Never invent product claims such as sterling silver, gold plated, waterproof, hypoallergenic, gemstone type, carat, or warranty unless confirmed by the user or reliable product information.

## 2. Identify the requested image type before generating

Do not treat every image as the same template. Identify the requested slot:

1. **Meet Lumière branded main image** — use the locked pale-mint brand template in meet-lumi-re/SKILL.md.
2. **Standard product main image** — use a clean white background only when requested or when the item is not using the Meet Lumière brand template.
3. **Single detail photo / macro** — one real product view focused on one construction or material detail.
4. **Feature detail infographic** — one coherent detail composition that explains one or two related functions using a large product hero plus a small inset/callout and concise English labels. This is one designed image, not a collage.
5. **Worn / scale image** — realistic human wear and correct product scale.
6. **Flat-lay image** — product resting naturally on a surface, with the full relevant silhouette visible.
7. **Lifestyle image** — restrained setting; jewelry remains the clear hero.

If the user asks for a detail image that combines a feature demonstration with a small close-up, use a feature detail infographic. Do not incorrectly force it into a single isolated macro.

## 3. Reference inspection and product lock

Before writing the image prompt:
1. Inspect every product photo supplied in the current task.
2. Identify what each photo actually proves: front, back, side, underside, worn scale, moving parts, opening, clasp, or setting.
3. Use close-ups for the exact details they show. Do not infer hidden construction from a front view.
4. Create a short product-lock checklist before generation.
5. Keep three categories separate: confirmed by photo, explicitly confirmed by the user, and unknown.
6. If a critical feature is not visible or references conflict, ask for the missing view or leave that feature unchanged. Never guess.

Reference priority:
1. Clear real-product photographs.
2. Close-up photographs of the exact feature being generated.
3. The user's explicit corrections and confirmations.
4. Earlier generated images, for composition only. A previous AI image is never more authoritative than the real product.

Use the supplied product photos as visual references in the image-generation/editing operation. A written description alone is not a substitute for the source photographs.

## 4. Universal product-lock instruction

Include this instruction in every image-generation prompt:

"Treat the user's real product photographs as the authoritative source of truth. Preserve the exact physical product, not an interpretation or redesign. Match the original silhouette, dimensions, proportions, thickness, component count and placement, stone count and arrangement, stone shape and color, setting and prong construction, metal color and finish, joints, layers, moving parts, openings, gaps, terminal ends, and all visible construction details. Do not add, remove, mirror, rotate, simplify, embellish, merge, separate, or rearrange any product component. Change only the camera angle, lighting, background, styling, or specific image defect requested by the user. If a feature is not established by the references, do not invent it."

For image polishing, add:
"Preserve every correct area of the source image. Make only the requested local correction; do not regenerate or alter the rest of the product."

For reference-led new-angle generation, add:
"A new camera viewpoint and environment are allowed. A new product design or altered construction is not."

For complex or distinctive geometry:
"Do not reconstruct the product from memory or from a generic jewelry archetype. Match the reference geometry literally. If exact preservation cannot be achieved through generation, use source-photo-based editing/retouching rather than inventing a replacement product."

## 5. Structural locks

Preserve:
- Outer silhouette, dimensions, proportions, thickness, width, curvature, and profile.
- Exact component count, positions, orientation, overlaps, offsets, and intentional asymmetry.
- Every stone's count, shape, size, color, direction, spacing, and setting.
- Prong count and placement, bezels, galleries, bridges, joints, hinges, and connections.
- Openings, gaps, clasps, terminal ends, and the way parts pass over or under each other.
- All moving or rotating parts and their relationship to fixed parts.

Never make the product larger, thicker, heavier, more symmetrical, more ornate, or more luxurious than the real item.

### Open-ended / adjustable rings
Inspect the actual close-up and preserve the exact:
- Location of the opening relative to the ring head.
- Gap width and direction.
- Number of ends and their exact terminal shape.
- End alignment, height, depth, and any overlap or crossing.
- Band thickness, curvature, taper, and surface finish.
- Relationship between the shank, ring head, and any secondary layer.

Do not move the opening to a more visually convenient position. Do not close the gap, add a hinge, invent a clasp, create extra band ends, or turn a layered construction into one solid piece. Do not assume two ends cross unless the source photo proves it.

### Product-specific lock card
When the user is working on the same four-petal rotating open-band ring documented in PRODUCT_LOCK_ROTATING_FOUR_PETAL_RING.md, read and apply that file in addition to these universal rules. Do not apply that ring's four-petal construction to other products.

## 6. Meet Lumière main image vs detail image

These are separate systems.

### Meet Lumière branded main image
Follow meet-lumi-re/SKILL.md and its approved template. The brand template is locked. Do not replace it with a generic white background, a new layout, a new logo, or a detail infographic unless the user explicitly requests a change.

### Detail images
Do not automatically use the pale-mint main-image template for detail images. Choose the background and layout to serve the feature being explained, while keeping the product faithful. For US-market detail graphics, all visible labels must be English.

## 7. Feature detail infographic — one composition, not a collage

Use this format when the user asks to explain a function and include a supporting close-up in the same image.

Required layout:
- One dominant, realistic product hero as the main visual.
- One secondary inset/callout for the supporting detail. The inset must remain clearly smaller than the hero and must not overpower it.
- A fine pointer, connector, or restrained highlight may connect the inset to the real feature location.
- Use short US-English labels only when they improve understanding.
- Keep generous negative space and a clear visual hierarchy.
- The composition must read as one designed product-detail image, not a grid, contact sheet, or unrelated multi-photo collage.

For the rotating four-petal ring:
- Make the complete ring the main visual.
- Use two restrained curved arrows around the flower face to communicate left-right rotation. Do not imply a full 360-degree rotation unless the user confirms it.
- Add a small inset showing the real C-shaped open-band gap near the back of the flower base.
- The open-band inset is a supporting detail, not the main oversized image.
- Suggested US-English labels: "Rotating Flower Top" and "Adjustable Open Band".
- Never show the open-band gap at the front of the ring or detach it from its real position.
- Do not use Chinese text.

## 8. Photography and gemstone realism

- Preserve the original metal color and realistic metal texture.
- Preserve the original gemstone hue and color family.
- Improve natural luster, facet definition, depth, and controlled reflections without changing stone identity.
- Do not use oversaturation to fake sparkle.
- Avoid blown highlights, white blobs, fake glow, excessive glitter, plastic-like surfaces, melted prongs, and impossible reflections.
- Props, hands, clothing, and graphic elements must not cover or deform the product.
- For worn images, use natural anatomy, believable finger/neck/ear proportions, and correct jewelry scale.

## 9. Image slot and composition rules

- Every output is one requested image file. Never return a contact sheet or an unsolicited collage.
- A feature detail infographic may contain one main product hero and a small related inset; this is not permission to create a multi-panel montage.
- Do not crop off a critical structural feature.
- Keep the whole product visible when the user asks for a full product view.
- For macro images, enlarge only the requested detail and keep its geometry readable.
- For flat-lays, the product must rest naturally; no floating, impossible bending, flattening, or reversed perspective.
- For lifestyle images, props must not touch, cover, or visually compete with the jewelry.

## 10. Export

- Default to a 1:1 image when the user has not specified a ratio.
- Preferred general export: at least 1000 × 1000 px, PNG or JPG, sRGB.
- Meet Lumière main images use the exact dimensions and layout specified in meet-lumi-re/SKILL.md.
- Do not claim a dimension, file format, color profile, file size, or platform compliance unless it has actually been verified.
- TikTok Shop requirements can change; check current Seller Center guidance before claiming compliance.

## 11. Mandatory quality gate before delivery

Compare the generated result directly against the supplied real-product references:

1. Correct product identity and silhouette.
2. Correct number and arrangement of all components and stones.
3. Correct dimensions, proportions, thickness, and curvature.
4. Correct metal color, gemstone hue, and surface finish.
5. Correct layers, joints, moving parts, opening position, gap, and terminal ends.
6. Correct requested image type and visual hierarchy.
7. Correct US-English spelling and wording; no Chinese characters unless explicitly requested.
8. No invented claims, extra jewelry, extra stones, fake hardware, or unsupported details.
9. No distortion, melted geometry, duplicate components, or AI artifacts.
10. Actual export specifications are known.

If any critical product feature fails:
- Do not deliver it as an accurate product image.
- Regenerate once with the exact failed feature described more explicitly.
- If it still fails, stop and explain the mismatch. Use source-photo editing or request a clearer reference instead of repeatedly inventing geometry.
- Never claim "100% identical", "perfectly accurate", or "ready to publish" without verification.

## 12. Delivery behavior

- When the user asks to generate an image, generate the image and display it directly in the conversation. Do not respond with only a prompt, a plan, or a description.
- Keep the delivery concise. The image should be the main response.
- After the image, briefly state the image type and any product detail that could not be verified.
- Do not claim a file was generated if no image-generation result was returned.
- If the user asks for one image, deliver one image—not several alternatives or a collage.
- The user-facing conversation may be Chinese, but customer-facing image copy defaults to US English.

## 13. Core operating rule

Product accuracy outranks styling. Correct the exact issue the user identifies and preserve every other correct feature. Re-inspect the relevant close-up before each correction. Never repeat a failed interpretation or present an unverified structure as fact.

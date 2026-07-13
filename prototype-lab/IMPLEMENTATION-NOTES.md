# Implementation notes

## Shopify-section candidates
- Header/city selector, hero blocks, trust strips, featured station grids, how-it-works, delivery/dietary confidence panels, FAQ accordions, large-event CTA and footer can become theme sections.
- Concept 2's reveal story can be built as reusable editorial image/text sections.

## JavaScript requirements
- City switching, mobile menu, quote modal, product quick-view drawer/toast, category filters and Concept 3 recommendations require JavaScript.
- The recommender can start as front-end rules mapped to Shopify product tags, then later become a more robust app or metaobject-driven module.

## Likely Shopify limitations
- Checkout/date/invoice logic should use existing Shopify checkout and apps, not be rebuilt in theme code.
- If city-specific inventory/pricing differs, a prototype city switch must map to actual Shopify markets, collections or product tags.
- Very theatrical scroll effects should be performance-tested on mobile before production.

## Assets reused
- Public CaterStation product names, prices, serving ranges, delivery/FAQ facts and brand language were reused.
- Real image download was attempted from the public site but blocked in the shell environment by network policy; prototypes use branded gradient placeholders labelled as image placeholders.

## Suggested implementation order
1. Choose hybrid IA: Concept 1 architecture plus Concept 3 recommendation module and selected Concept 2 reveal moments.
2. Build city-aware header, headcount taxonomy and product card redesign.
3. Add delivery/dietary/invoice confidence strips above product discovery.
4. Implement quote modal/large-event route.
5. Add editorial reveal sections and replace placeholders with approved Shopify CDN assets.

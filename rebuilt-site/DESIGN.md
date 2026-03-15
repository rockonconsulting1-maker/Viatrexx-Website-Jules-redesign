# Viatrexx USA Design System - Source of Truth

## Core Principles
1. **Clarity & Trust:** Use medical-grade typography and clear layouts.
2. **Integrative Approach:** Blend natural teal/cyan gradients with professional blues.
3. **Responsive first:** Ensure all components work across devices (inherited from GHL/Nuxt).

## 1. Color Palette

### Primary Colors
- **Primary Blue:** `#0056B3` - Main brand color (Brand Professional)
- **Primary Dark Blue:** `#004494` - Hover states / Emphasis
- **Action Blue:** `#188BF6` - GHL UI interactions / Secondary actions

### Functional Colors
- **Text (Dark):** `#2C3E50`
- **Text (Muted):** `#667085`
- **Background (Light):** `#F8F9FA`
- **Border:** `#D1D5DB` (Gray-300)
- **Error/Danger:** `#F87171` (Red-400)

### Gradients (Wellness Spectrum)
- **Gradient 1:** `#3B82F6` (Blue)
- **Gradient 2:** `#556270` (Steel)
- **Gradient 3:** `#4ECDC4` (Teal)
- **Gradient 4:** `#22D3EE` (Cyan)
- **Gradient 5:** `#8B5CF6` (Violet)
- **Gradient 6:** `#0D47A1` (Deep Blue)

## 2. Typography

### Headline Font
- **Family:** `Montserrat`, sans-serif
- **Weights:** 500 (Medium), 600 (Semi-Bold), 700 (Bold)

### Content Font
- **Family:** `Inter`, sans-serif (Modern Standard)
- **Fallback:** `Lato`, sans-serif (Legacy compatibility)
- **Weights:** 400 (Regular), 500 (Medium)

### Scale
- **Base Size:** 16px (rem based)
- **Small Text:** 14px
- **H1:** 2.25rem (36px)
- **H2:** 1.875rem (30px)
- **H3:** 1.5rem (24px)

## 3. Layout & Spacing

### Containers
- **Max Width:** `1170px` (Standard Content)
- **Section Max Width:** `1120px` (Feature sections)
- **Gutter:** `15px` (on each side)

### Surface & Border
- **Radius (Small):** `0.5rem` (8px) - Buttons, Inputs
- **Radius (Medium):** `0.75rem` (12px) - Cards, Sidebar
- **Shadow (Soft):** `0 4px 6px -1px rgba(0, 0, 0, 0.1)`

## 4. Design Anti-patterns to Resolve
- **Redundant Font Loads:** Remove Lato/Open Sans/Roboto if Inter/Montserrat cover all needs.
- **!important Overuse:** Refactor CSS to use specificity or utility classes.
- **Hard-coded Pixels:** Transition from `px` to `rem` for spacing and font sizes.

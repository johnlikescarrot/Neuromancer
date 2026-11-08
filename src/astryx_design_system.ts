/**
 * Astryx Design System - Cyberpunk Academic Tokens & Layout Configurations
 * Based on Meta's Astryx Design System tokens, typography, and component styling.
 */

export interface DesignTokens {
  colors: {
    primary: string;
    primaryMuted: string;
    accent: string;
    accentGlow: string;
    bgDark: string;
    bgCard: string;
    bgHover: string;
    bgLightEn: string;
    bgLightVi: string;
    borderMuted: string;
    borderStrong: string;
    textPrimary: string;
    textSecondary: string;
    textMuted: string;
    badgeBg: string;
    badgeText: string;
  };
  typography: {
    fontSans: string;
    fontSerif: string;
    fontMono: string;
    fontSizeBody: string;
    fontSizeH1: string;
    fontSizeH2: string;
    fontSizeH3: string;
    lineHeightBody: string;
  };
  spacing: {
    pagePadding: string;
    gapColumn: string;
    cardPadding: string;
    radiusSm: string;
    radiusMd: string;
    radiusLg: string;
  };
}

export const AstryxCyberpunkTheme: DesignTokens = {
  colors: {
    primary: '#0284c7',       // Sky 600
    primaryMuted: '#0369a1',  // Sky 700
    accent: '#06b6d4',        // Cyan 500
    accentGlow: '#22d3ee',    // Cyan 400
    bgDark: '#0b132b',        // Deep Space Navy
    bgCard: '#f8fafc',        // Slate 50
    bgHover: '#f1f5f9',       // Slate 100
    bgLightEn: '#ffffff',     // Pure White
    bgLightVi: '#f8fafc',     // Subdued Slate 50
    borderMuted: '#cbd5e1',   // Slate 300
    borderStrong: '#0284c7',  // Astryx Accent
    textPrimary: '#0f172a',   // Slate 900
    textSecondary: '#334155', // Slate 700
    textMuted: '#64748b',     // Slate 500
    badgeBg: '#0f172a',       // Slate 900
    badgeText: '#38bdf8',     // Sky 400
  },
  typography: {
    fontSans: "'Liberation Sans', 'DejaVu Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
    fontSerif: "'Liberation Serif', 'Georgia', 'DejaVu Serif', serif",
    fontMono: "'Liberation Mono', 'DejaVu Sans Mono', 'Courier New', monospace",
    fontSizeBody: '9.6pt',
    fontSizeH1: '28pt',
    fontSizeH2: '16pt',
    fontSizeH3: '12pt',
    lineHeightBody: '1.55',
  },
  spacing: {
    pagePadding: '1.8cm 1.5cm 2cm 1.5cm',
    gapColumn: '16px',
    cardPadding: '14px 18px',
    radiusSm: '4px',
    radiusMd: '8px',
    radiusLg: '12px',
  },
};

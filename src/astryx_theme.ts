/**
 * Astryx Design System - Theme Tokens & Academic Bilingual Component Styles
 * Inspired by @astryxdesign/core and @astryxdesign/theme-neutral
 * Custom property definitions for high-legibility dual-language publications
 */
export const astryxTokens = {
  colors: {
    // Cyberpunk & Academic Palette
    primary: '#0f172a',        // Slate 900
    primaryLight: '#1e293b',   // Slate 800
    accent: '#0284c7',         // Sky 600
    accentCyan: '#06b6d4',     // Cyan 500
    accentWarm: '#ea580c',     // Orange 600
    bgLight: '#ffffff',
    bgSubtle: '#f8fafc',       // Slate 50
    bgCard: '#f1f5f9',         // Slate 100
    borderMuted: '#cbd5e1',    // Slate 300
    borderAccent: '#38bdf8',   // Sky 400
    textPrimary: '#0f172a',
    textSecondary: '#475569',  // Slate 600
    textMuted: '#64748b',      // Slate 500
    codeGreen: '#047857',      // Emerald 700
    highlightBg: '#e0f2fe',    // Sky 100
    highlightText: '#0369a1',  // Sky 700
  },
  typography: {
    fontBody: "'Liberation Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif",
    fontHeading: "'Liberation Serif', Georgia, Cambria, 'Times New Roman', Times, serif",
    fontMono: "'Liberation Mono', Menlo, Monaco, Consolas, 'Courier New', monospace",
  },
  spacing: {
    xs: '4px',
    sm: '8px',
    md: '16px',
    lg: '24px',
    xl: '32px',
    xxl: '48px',
  },
  shadows: {
    card: '0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05)',
    elevation: '0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04)',
  }
};

export function generateAstryxCSS(): string {
  return `
    :root {
      --astryx-color-primary: ${astryxTokens.colors.primary};
      --astryx-color-primary-light: ${astryxTokens.colors.primaryLight};
      --astryx-color-accent: ${astryxTokens.colors.accent};
      --astryx-color-accent-cyan: ${astryxTokens.colors.accentCyan};
      --astryx-color-accent-warm: ${astryxTokens.colors.accentWarm};
      --astryx-color-bg-subtle: ${astryxTokens.colors.bgSubtle};
      --astryx-color-bg-card: ${astryxTokens.colors.bgCard};
      --astryx-color-border-muted: ${astryxTokens.colors.borderMuted};
      --astryx-color-text-primary: ${astryxTokens.colors.textPrimary};
      --astryx-color-text-secondary: ${astryxTokens.colors.textSecondary};
      --astryx-font-body: ${astryxTokens.typography.fontBody};
      --astryx-font-heading: ${astryxTokens.typography.fontHeading};
      --astryx-font-mono: ${astryxTokens.typography.fontMono};
    }

    @page {
      size: A4;
      margin: 1.8cm 1.5cm 2cm 1.5cm;
      @bottom-center {
        content: counter(page);
        font-size: 9pt;
        color: var(--astryx-color-text-secondary);
        font-family: var(--astryx-font-body);
      }
    }

    *, *::before, *::after {
      box-sizing: border-box;
    }

    body {
      font-family: var(--astryx-font-body);
      color: var(--astryx-color-text-primary);
      line-height: 1.6;
      background: #ffffff;
      margin: 0;
      padding: 0;
      font-size: 10pt;
      -webkit-font-smoothing: antialiased;
    }

    /* Cover Page - Astryx Editorial Style */
    .cover-page {
      page-break-after: always;
      height: 95vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 40px 24px;
      border: 3px double var(--astryx-color-primary);
      background: linear-gradient(180deg, #f8fafc 0%, #e2e8f0 100%);
      border-radius: 8px;
    }

    .cover-badge-top {
      background: var(--astryx-color-primary);
      color: var(--astryx-color-accent-cyan);
      font-size: 8.5pt;
      font-weight: 700;
      letter-spacing: 2px;
      padding: 4px 14px;
      border-radius: 9999px;
      text-transform: uppercase;
      margin-bottom: 24px;
    }

    .cover-title {
      font-size: 40pt;
      font-weight: 900;
      letter-spacing: 4px;
      text-transform: uppercase;
      color: var(--astryx-color-primary);
      margin-bottom: 6px;
      font-family: var(--astryx-font-heading);
    }

    .cover-sub {
      font-size: 17pt;
      font-weight: 700;
      color: #1e293b;
      margin-bottom: 24px;
      letter-spacing: 1px;
    }

    .cover-author {
      font-size: 15pt;
      font-style: italic;
      color: #334155;
      margin-bottom: 36px;
    }

    .cover-desc {
      max-width: 680px;
      font-size: 10.5pt;
      line-height: 1.65;
      color: #1e293b;
      background: rgba(255, 255, 255, 0.92);
      padding: 24px 28px;
      border-radius: 8px;
      box-shadow: ${astryxTokens.shadows.elevation};
      border: 1px solid var(--astryx-color-border-muted);
      margin-bottom: 28px;
    }

    .badge-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
      margin-top: 18px;
    }

    .badge {
      background: var(--astryx-color-primary);
      color: #38bdf8;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 9pt;
      border: 1px solid #334155;
      box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }

    /* Academic Study Section */
    .section-page {
      page-break-before: always;
      page-break-after: always;
    }

    .intro-box {
      background: var(--astryx-color-bg-card);
      border-left: 5px solid var(--astryx-color-accent);
      padding: 18px 22px;
      margin-bottom: 24px;
      border-radius: 0 8px 8px 0;
      box-shadow: ${astryxTokens.shadows.card};
    }

    .intro-title {
      font-size: 17pt;
      font-weight: 800;
      color: var(--astryx-color-primary);
      margin-top: 0;
      margin-bottom: 12px;
    }

    /* Table of Contents */
    .toc-list {
      list-style: none;
      padding: 0;
      columns: 2;
      column-gap: 32px;
    }

    .toc-item {
      margin-bottom: 12px;
      font-size: 9.5pt;
      break-inside: avoid;
    }

    .toc-link {
      text-decoration: none;
      color: #0369a1;
      font-weight: 600;
    }

    /* Part Header - High Impact Astryx Banner */
    .part-header {
      page-break-before: always;
      background: var(--astryx-color-primary);
      color: #ffffff;
      padding: 32px 24px;
      text-align: center;
      border-radius: 8px;
      margin-bottom: 28px;
      border-bottom: 4px solid var(--astryx-color-accent-cyan);
    }

    .part-title-en {
      font-size: 18pt;
      letter-spacing: 2px;
      font-weight: 800;
      color: #38bdf8;
      margin: 0 0 8px 0;
      text-transform: uppercase;
    }

    .part-title-vi {
      font-size: 14pt;
      font-weight: 600;
      color: #e2e8f0;
      margin: 0;
    }

    /* Chapter Header */
    .chapter-container {
      margin-bottom: 36px;
      page-break-inside: auto;
    }

    .chapter-header {
      background: var(--astryx-color-bg-subtle);
      border-bottom: 2px solid var(--astryx-color-border-muted);
      padding: 16px 20px;
      margin-top: 32px;
      margin-bottom: 20px;
      border-left: 6px solid #2563eb;
      page-break-after: avoid;
      border-radius: 0 6px 6px 0;
    }

    .chap-title-en {
      font-size: 16pt;
      font-weight: 800;
      color: #1e3a8a;
      margin: 0 0 4px 0;
    }

    .chap-title-vi {
      font-size: 12pt;
      color: #475569;
      font-weight: 600;
      margin: 0;
    }

    /* Study Guide Card */
    .study-guide-card {
      background: #fffbeb;
      border: 1px solid #fde68a;
      border-left: 5px solid #d97706;
      padding: 16px 20px;
      margin-bottom: 24px;
      border-radius: 6px;
      page-break-inside: avoid;
      box-shadow: ${astryxTokens.shadows.card};
    }

    .study-title {
      font-size: 10.5pt;
      font-weight: 800;
      color: #b45309;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-top: 0;
      margin-bottom: 8px;
    }

    .study-summary {
      font-size: 9.6pt;
      color: #334155;
      margin-bottom: 12px;
      line-height: 1.55;
    }

    .grammar-item {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      padding: 10px 14px;
      margin-bottom: 8px;
      border-radius: 6px;
      font-size: 9.2pt;
    }

    .grammar-name {
      font-weight: 700;
      color: #1d4ed8;
    }

    .grammar-eg {
      font-style: italic;
      color: ${astryxTokens.colors.codeGreen};
      margin-top: 4px;
    }

    /* Parallel Bilingual Grid */
    .bilingual-pair {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 14px;
      page-break-inside: avoid;
      align-items: stretch;
    }

    .col-en {
      flex: 1;
      background: #ffffff;
      padding: 9px 13px;
      border-left: 2px solid #94a3b8;
      font-size: 9.6pt;
      text-align: justify;
      line-height: 1.58;
      color: #0f172a;
    }

    .col-vi {
      flex: 1;
      background: #f8fafc;
      padding: 9px 13px;
      border-left: 2px solid #3b82f6;
      font-size: 9.6pt;
      text-align: justify;
      line-height: 1.58;
      color: #1e293b;
    }

    .vocab-pill {
      background: #e0f2fe;
      color: #0369a1;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 8.5pt;
      font-weight: 700;
      margin-right: 4px;
      display: inline-block;
      border: 1px solid #bae6fd;
    }

    .term-highlight {
      background: #fef08a;
      color: #713f12;
      padding: 1px 4px;
      border-radius: 3px;
      font-weight: 600;
    }

    /* Academic Glossary Table */
    .glossary-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 16px;
      font-size: 9pt;
      border-radius: 6px;
      overflow: hidden;
    }

    .glossary-table th {
      background: var(--astryx-color-primary);
      color: #ffffff;
      padding: 10px 12px;
      text-align: left;
      border: 1px solid #334155;
      font-weight: 700;
    }

    .glossary-table td {
      padding: 9px 12px;
      border: 1px solid #cbd5e1;
      vertical-align: top;
    }

    .glossary-table tr:nth-child(even) {
      background: #f8fafc;
    }
  `;
}

"""Bolt.new AIアプリビルダー完全ガイド - プロンプト定義

Bolt.new特化ブログ用のプロンプトを一元管理する。
JSON-LD構造化データ（BlogPosting / FAQPage / BreadcrumbList）対応。
"""

# ペルソナ設定
PERSONA = (
    "あなたはBolt.newとAIアプリビルダーの日本語エキスパートです。"
    "バイブコーディング（プロンプトだけでアプリを作る手法）に精通し、"
    "Bolt.new・Lovable・Replit・Cursorなどの最新ツールを使いこなすプロのテックライターです。"
    "非エンジニアでもわかるように、フルスタックアプリの自動生成・デプロイまでを丁寧に解説できます。"
    "Next.js、React、Supabase等のモダン技術スタックにも詳しく、"
    "実践的なプロンプト例とともに読者をガイドします。"
)

# 記事フォーマット指示
ARTICLE_FORMAT = """
【記事構成（必ずこの順序で書くこと）】

## この記事でわかること
- ポイント1（具体的なベネフィット）
- ポイント2
- ポイント3

## 結論（先に結論を述べる）
（読者が最も知りたい答えを最初に提示）

## 本題（H2で3〜5セクション）
（具体的な手順・解説。実際のプロンプト例を含めて操作手順を箇条書きで明示）

## プロンプト実例集
（コピペで使えるBolt.new向けプロンプトを3つ以上紹介）

## 他のAIビルダーとの比較
（Lovable / Replit / Cursor / v0 との違いを表形式で整理）

## よくある質問（FAQ）
### Q1: （よくある質問1）
A1: （回答1）

### Q2: （よくある質問2）
A2: （回答2）

### Q3: （よくある質問3）
A3: （回答3）

## まとめ
（要点整理と次のアクション提案）
"""

# カテゴリ別SEOキーワードヒント
CATEGORY_PROMPTS = {
    "Bolt.new 使い方": "Bolt.new 使い方、Bolt.new 始め方、Bolt.new 初心者、Bolt.new 無料、Bolt.new ブラウザ アプリ生成",
    "Bolt.new 料金・プラン": "Bolt.new 料金、Bolt.new 無料 有料 違い、Bolt.new Pro プラン、Bolt.new トークン 月額",
    "Bolt.new vs Lovable": "Bolt.new Lovable 比較、Bolt.new Lovable 違い、AIアプリビルダー 比較 2026、どっちがいい",
    "Bolt.new 最新ニュース": "Bolt.new アップデート、Bolt.new 新機能、StackBlitz AI 最新、Bolt.new リリース",
    "バイブコーディング": "バイブコーディング、vibe coding、プロンプト アプリ開発、AI コーディング 自然言語",
    "Bolt.new テクニック": "Bolt.new プロンプト テクニック、Bolt.new Next.js React、Bolt.new デプロイ、Bolt.new Supabase",
    "AIアプリビルダー比較": "AIアプリビルダー おすすめ、Bolt.new Cursor Replit 比較、AI コード生成 ランキング 2026",
    "Bolt.new 活用事例": "Bolt.new ビジネス活用、Bolt.new SaaS 作成、Bolt.new ポートフォリオ、AI アプリ 事例",
}

# ニュースソース
NEWS_SOURCES = [
    "StackBlitz Blog (https://blog.stackblitz.com/)",
    "Bolt.new公式 (https://bolt.new/)",
    "TechCrunch (https://techcrunch.com/)",
    "The Verge (https://www.theverge.com/)",
    "Product Hunt (https://www.producthunt.com/)",
]

# FAQ構造化データの有効化
FAQ_SCHEMA_ENABLED = True

# キーワード選定用の追加プロンプト
KEYWORD_PROMPT_EXTRA = (
    "Bolt.new（AIアプリビルダー）に関するキーワードを選んでください。\n"
    "日本のユーザーが検索しそうな実用的なキーワードを意識してください。\n"
    "「Bolt.new 使い方」「Bolt.new 料金」「Bolt.new vs Lovable」のような、\n"
    "検索ボリュームが見込めるキーワードを優先してください。\n"
    "バイブコーディング・ノーコード・AIコーディングの文脈も考慮してください。"
)


def build_keyword_prompt(config):
    """キーワード選定プロンプトを構築する"""
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    category_hints = "\n".join(
        f"- {cat}: {hints}" for cat, hints in CATEGORY_PROMPTS.items()
    )
    return (
        f"{PERSONA}\n\n"
        "Bolt.new AIアプリビルダー完全ガイド用のキーワードを選定してください。\n\n"
        f"{KEYWORD_PROMPT_EXTRA}\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        f"カテゴリ別キーワードヒント:\n{category_hints}\n\n"
        "以下の形式でJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )


def build_article_prompt(keyword, category, config):
    """Bolt.new特化記事生成プロンプトを構築する"""
    category_hints = CATEGORY_PROMPTS.get(category, "")
    news_sources_text = "\n".join(f"- {src}" for src in NEWS_SOURCES)

    return f"""{PERSONA}

以下のキーワードに関する記事を、Bolt.new AIアプリビルダー専門サイト向けに執筆してください。

【基本条件】
- ブログ名: {config.BLOG_NAME}
- キーワード: {keyword}
- カテゴリ: {category}
- カテゴリ関連キーワード: {category_hints}
- 言語: 日本語
- 文字数: {config.MAX_ARTICLE_LENGTH}文字程度

{ARTICLE_FORMAT}

【SEO要件】
1. タイトルにキーワード「{keyword}」を必ず含めること
2. タイトルは32文字以内で魅力的に（数字や年号を含めると効果的）
3. H2、H3の見出し構造を適切に使用すること
4. キーワード密度は{config.MIN_KEYWORD_DENSITY}%〜{config.MAX_KEYWORD_DENSITY}%を目安に
5. メタディスクリプションは{config.META_DESCRIPTION_LENGTH}文字以内
6. FAQ（よくある質問）を3つ以上含めること（FAQPage構造化データ対応）

【内部リンク】
- 内部リンクのプレースホルダーを2〜3箇所に配置（{{{{internal_link:関連トピック}}}}の形式）

【参考情報源】
{news_sources_text}

【条件】
- {config.MAX_ARTICLE_LENGTH}文字程度
- 2026年最新の情報を反映すること
- 具体的なプロンプト例を含めること（コピペで使えるもの）
- Bolt.newでの実際の操作手順やスクリーンショットの代替説明を含める
- 他のAIビルダー（Lovable, Replit, Cursor, v0）との客観的な比較を含める
- 非エンジニアにもわかりやすく、専門用語には補足説明を付ける

【出力形式】
以下のJSON形式で出力してください。JSONブロック以外のテキストは出力しないでください。

```json
{{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "faq": [
    {{"question": "質問1", "answer": "回答1"}},
    {{"question": "質問2", "answer": "回答2"}},
    {{"question": "質問3", "answer": "回答3"}}
  ]
}}
```

【注意事項】
- content内のMarkdownは適切にエスケープしてJSON文字列として有効にすること
- tagsは5個ちょうど生成すること
- slugは半角英数字とハイフンのみ使用すること
- faqは3個以上生成すること（FAQPage構造化データに使用）
- 読者にとって実用的で具体的な内容を心がけること"""

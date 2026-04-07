"""Bolt.new AIアプリビルダー完全ガイド - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "Bolt.new AIアプリビルダー完全ガイド"
BLOG_DESCRIPTION = "ブラウザでAIアプリを即生成するBolt.newの使い方・最新機能・Lovable比較を毎日更新。プロンプトだけでフルスタックアプリを作る方法を完全解説。"
BLOG_URL = "https://musclelove-777.github.io/bolt-new-guide"
BLOG_TAGLINE = "プロンプトだけでフルスタックアプリを作る最強AIビルダー"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/bolt-new-guide"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "Bolt.new 使い方",
    "Bolt.new 料金・プラン",
    "Bolt.new vs Lovable",
    "Bolt.new 最新ニュース",
    "バイブコーディング",
    "Bolt.new テクニック",
    "AIアプリビルダー比較",
    "Bolt.new 活用事例",
]

THEME = {
    "primary": "#1389FD",
    "accent": "#00e5ff",
    "gradient_start": "#1389FD",
    "gradient_end": "#00e5ff",
    "dark_bg": "#0a0f1e",
    "dark_surface": "#141e30",
    "light_bg": "#f0f8ff",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 1
SCHEDULE_HOURS = [12]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Bolt.new Pro": [
        {"service": "Bolt.new", "url": "https://bolt.new", "description": "Bolt.newでAIアプリを作る"},
    ],
    "StackBlitz": [
        {"service": "StackBlitz", "url": "https://stackblitz.com", "description": "StackBlitzでWebIDEを使う"},
    ],
    "Vercel": [
        {"service": "Vercel", "url": "https://vercel.com", "description": "Vercelにデプロイする"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "UdemyでAI開発講座を探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAI関連書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAI関連書籍を探す"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8104

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-HJLCFVY5TF"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}

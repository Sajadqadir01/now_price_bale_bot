# now price bale bot

یک ربات بله چندزبانه که از APIهای [Nerkh.io](https://nerkh.io) و بله استفاده می‌کند.

## پیش‌نیازها (Prerequisites)

*   **Python 3.12+:** اطمینان حاصل کنید که نسخه پایتون شما 3.7 یا بالاتر است.
*   **Pip:** پکیج منیجر پیش‌فرض پایتون.
*   **حساب کاربری در Nerkh.io:** برای دریافت API Key.
*   **بازو بله:** برای دریافت API Token از طریق @BotFather در پبامرسان بله.

## نصب (Installation)

1.  **کلون کردن مخزن:**
    ```bash
    git clone https://github.com/yourusername/now_price_bale_bot.git
    cd now_price_bale_bot
    ```
    (آدرس گیت خود را جایگزین کنید)

2.  **نصب وابستگی‌ها:**
    ```bash
    pip install -r requirements.txt
    ```
    *توضیح:* فایل `requirements.txt` باید حاوی پکیج‌هایی مانند `python-telegram-bot`, `requests`, `python-dotenv` و غیره باشد. اگر این فایل را ندارید، با دستور `pip install python-telegram-bot python-dotenv requests` پکیج‌های لازم را نصب کنید و سپس نام آن‌ها را در فایلی به نام `requirements.txt` قرار دهید.

## پیکربندی (Configuration)

1.  **ایجاد فایل `.env`:**
    در **ریشه پروژه** (همان پوشه‌ای که فایل README.md در آن قرار دارد)، فایلی به نام `.env` ایجاد کنید.

2.  **تنظیم مقادیر API:**
    محتوای فایل `.env` را به صورت زیر تنظیم کنید و مقادیر واقعی را جایگزین نمایید:

    ```env
    # API Key از سایت nerkh.io
    API_KEY=your_nerkh_api_key_here

    # API Token از @BotFather بله
    API_TOKEN=your_bale_bot_token_here
    ```

    *   **`API_KEY`:** این کلید را از داشبورد حساب کاربری خود در [Nerkh.io](https://nerkh.io) دریافت کنید.
    *   **`API_TOKEN`:** این توکن را با صحبت کردن با ربات [@BotFather](https://bale.ai/botfather) در بله دریافت کنید (با دستور `/newbot`).

## نحوه استفاده (Usage)

پس از انجام مراحل نصب و پیکربندی، ربات شما آماده اجرا است.

1.  **اجرای ربات:**
    ```bash
    python main.py
    ```
    (نام فایل اصلی ربات خود را جایگزین کنید)

2.  **ارتباط با ربات:**
    ربات خود را در تلگرام پیدا کنید و با آن تعامل کنید. دستورات اولیه مانند `/start` و `/language` که در کد ربات تعریف شده‌اند، باید کار کنند.

## جزئیات مربوط به Nerkh.io

تمامی عملیات مربوط به دریافت نرخ‌ها، اطلاعات و سایر سرویس‌ها توسط API های [Nerkh.io](https://nerkh.io) مدیریت می‌شود. ربات شما از `API_KEY` برای احراز هویت و دسترسی به این سرویس‌ها استفاده می‌کند. جزئیات مربوط به توابع و داده‌های موجود در API نرخ‌های ارز و طلا را می‌توانید در مستندات رسمی [Nerkh.io](https://nerkh.io) مشاهده فرمایید.

## مشارکت (Contributing)

ما از مشارکت‌های شما استقبال می‌کنیم! اگر ایده‌ای برای بهبود دارید یا با مشکلی مواجه شدید، لطفاً یک "Issue" ثبت کنید یا یک "Pull Request" ارسال نمایید.


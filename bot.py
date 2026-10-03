from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = "8584951695:AAFJ54L1YDFicCBYo6NDIc9-IfIR0JKD1Yg"

# القائمة الرئيسية للبوت
main_menu = [
    ["عِلْمِي... 💙", "أدبي... 🖤"],
    ["منوعات... 🎁"],
    ["بحث عن كتاب 🔍"],
    ["المكتبة 📚🌱"],
    ["أضف كتاب 📥📕", "اطلب كتاب 🔍📕"],
    ["بوكليتات 2024 🔥", "بوكليتات 2025 🔥"],
    ["للـتـواصـل معـنا 🤝"],
    ["مطور البوت ✨❤️"]
]

# قائمة أقسام المكتبة العامة
library_menu = [
    ["أعمال أدهم شرقاوي 📚"],
    ["رسالة لك | 🌱🤎|"],
    ["| الرُّوايات | 💌❤️", "| كُتُبٌ مُنَوَّعَةٌ | 💛🤎"],
    ["| النُّصُوصُ وَالْخَوَاطِرُ | 🍿", "| الْمَكْتَبَةُ الْإِسْلَامِيَّةُ | 🕋"],
    ["| اَلْأَدَبُ وَالشِّعْرُ | 📜🤎", "| كُتُبٌ الْمَرْأَةِ | 👗"],
    ["| كتاب في دقائق |.. 📖✨"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

# قائمة كتب منوعة (الصفحة الأولى)
diverse_books_menu = [
    ["وطن يشبه عينيك 🍩🤎"],
    ["لماذا الشوكة لا مذاق لها 🥯", "الأب الغني والأب الفقير 🤑"],
    ["افضل نسخه منك 🦅", "اعرف وجهك الآخر 🎭", "أخبرني لماذا 📍?!"],
    ["154 كلمه لقول افتقدتك 💔🤎"],
    ["عندما يعشق الرجل 🖤", "لماذا ننام 😴", "عالم صوفي 🌊❤️"],
    ["ماذا لو 🥀", "في الجامعة 💬", "رحلة عقل 🌊"],
    ["لُغة الحزن 🖤", "البداية والنهاية 💌", "الادراك الجهنمي 🧠"],
    ["إدارة الأولويات 💖", "فن اللامبالاة 🤎🧠", "أعد التفكير ✍️"],
    ["العادات الذرية 🖤", "الليالي البيضاء 🤍🌱", "اكستاسي 🖤"],
    ["الف ليلة وليلة 💫", "25 قصة نجاح 📖📗", "مميز بالأصفر 📗"],
    ["العادات السبع ❤", "أشياء لا تعرفها 📗"],
    ["كن بخير 👑", "إكتشف شغفك 🔵", "استرجع قلبك 💌❤️"],
    ["هؤلاء علموني للموت 📗", "30 طريقة 📗", "ملهمون 📗"],
    ["| المزيد من الكتب المنوعة | ⭐"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

# قائمة كتب منوعة (الصفحة الثانية)
diverse_books_page2 = [
    ["الست قطاً 📗", "هذا الكتاب سيؤلمك 📗"],
    ["أزمة منتصف العمر الرائعة 💫", "إبق قويّاً 365 يوماً في السنة 🪬"],
    ["أشياء غريبة لم تعرفها من قبل 🕯️", "موعد مع فتاة تحب الكتابة 🦋"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

# قائمة الروايات الموسعة بدقة
novels_menu = [
    ["رواية شمس | 🤍☀️|"],
    ["| المزيد من اِلرُّؤايات | ❤️"],
    ["روايات عالمية | 📜🌍|", "📚 روايات أحمد آل حمدان 📚"],
    ["رواية \"055\" شهد قربان 🦋"],
    ["حديث القمر 🌙", "أشباح طينية 👻", "عتبة الألم 🕯️"],
    ["رواية 11:11 ⏰", "هاملت 🎭", "ذاكرة الجسد 🌿"],
    ["الآن أفهم 🖤", "لستُ آسفة 💔", "الحفرة 🕳️"],
    ["قصة حب مجوسية 💛", "الثقوب السوداء 🌌"],
    ["وراء الباب المغلق 🚪"],
    ["رواية الموتى - رعب وإثارة 🔥"],
    ["ديوان الجواهري #1 🪵", "ديوان الجواهري #2 🪵"],
    ["رسالة إلى 🚶‍♂️📄", "خوف 🖤🔗", "ضننته حبًّا 👼❤️"],
    ["عن شيء اسمه الحب ❤️", "نظرية الفسق - رواية مرعبة 📘"],
    ["ما مغامرة المقبرة الفرعونية 😐⚰️"],
    ["جاري الكتابة 🧡🌿", "معنى أن تكون وحيداً 🚶‍♂️💙"],
    ["أرض زيكولا ❤.", "بحث عنك 🧡🔍"],
    ["لا تقرب النساء قبل سن الـ 25 🌱💚"],
    ["غربة الياسمين 🥀❤️", "رواية ألف 🌿💜"],
    ["قطراتك بلسم جراحي 🙁💔💧"],
    ["حكاية قلب 💙🫀❤️"],
    ["وتلاقت الندوب لتنمحي 🚶‍♂️💔"],
    ["ظل الرياح 🤍🌬️", "الوجه الآخر للحب 💕"],
    ["🔙 رجوع", "القائمة الرئيسية 🔝"]
]

# قائمة النصوص والخواطر الموسعة
texts_menu = [
    ["ليتها تقرأُ 🖤", "حبيبتي قارئة ❤️"],
    ["ما لا يقال 💔"],
    ["في عقيدة الحب كلنا يهود 🖤🔒"],
    ["عن أشياء تؤلمك 🤎", "كن لنفسك كل شئ ❤️‍🩹"],
    ["تمهل أيها الفأس إن نصفك شجرة 🪓"],
    ["خواطر للحياة ⚖️"],
    ["عذراً إذا انقطع الكلام 🗣️💙", "شيء من أثر الغياب 🧣🖤"],
    ["شغف 🤍🫀"],
    ["كاردل 🖤", "97 تنهيدة 🤎", "وجع غافي ❤️‍🩹"],
    ["🔙 رجوع", "القائمة الرئيسية 🔝"]
]

# قائمة المكتبة الإسلامية الرئيسية
islamic_library_menu = [
    ["تفسير القرآن الكريم 📖"],
    ["| كُتُبٌ إِسْلَامِيَّةٌ | 🕋"],
    ["🔙 رجوع", "القائمة الرئيسية 🔝"]
]

# قائمة كتب إسلامية
islamic_books_menu = [
    ["الريح العاتية ⚔️️🖤"],
    ["تحت اجنحه البرزخ 🌸"],
    ["الداء والدواء ❤"],
    ["كوني صحابية ❤️🌸"],
    ["لانك الله ✨🫀"],
    ["معجزات الذكر ❤️", "ما لا يسع المسلم جهله 💜"],
    ["أول مرا أتدبر القرآن 🤍🕋"],
    ["لله نمضي 💙"],
    ["في قصصهم عبرة 🌱💚", "ملخص منهاج السنة 💙"],
    ["إن ربي لطيف 🤎", "إلى الله 🧡"],
    ["أجمل البشرى بأعظم الأذكار أجراً 🧡"],
    ["🔙 رجوع", "القائمة الرئيسية 🔝"]
]

# قائمة تفسير القرآن الكريم
quran_tafsir_menu = [
    ["ابن تيمية 🔶"],
    ["محمد راتب النابلسي 🔶", "ابن عثيمين 🔹"],
    ["عثمان الخميس 🔶", "محمد متولي الشعراوي 🔹"],
    ["🔙 رجوع", "القائمة الرئيسية 🔝"]
]

# قائمة الأدب والشعر
literature_poetry_menu = [
    ["| اَلْأَدَبُ اَلسَّاخِرُ | 🎭"],
    ["نجيب محفوظ 📚🥀", "نزار قباني 📚🥀"],
    ["محمود درويش 📚🥀"],
    ["ديوان المتنبي 🌱"],
    ["🔙 رجوع", "القائمة الرئيسية 🔝"]
]

# قائمة كتب المرأة
womens_books_menu = [
    ["| التجميل والمكياج | 💄", "| كتب تعليم الطبخ | 🍔"],
    ["أستطيع أن أجعلك نحيلة"],
    ["أكثر من 1000 جواب للمرأة المسلمة 🧕🕋"],
    ["أنثى مخملية 🕯️", "أنوثة طاغية 💫", "كاريزما الأنوثة 💅"],
    ["🔙 رجوع", "القائمة الرئيسية 🔝"]
]

variety_menu = [
    ["نصائح... ❤", "تحدي الـ30 يوم 💼"],
    ["كتكوتي... 🐥"],
    ["تنسيق 2024 📊", "تنسيق 2023 📊"],
    ["تنسيق 2022 📊", "تنسيق 2021 📊"],
    ["أفضل المدرسين... ❤️"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

# قائمة النصائح بالترتيب المطابق للصورة تماماً
tips_menu = [
    ["مشاكل وحلها 🥇", "اسئلة واجاباتها 🥇"],
    ["نصائح للثانوية 🥇", "جداول مذاكرة 🥇"],
    ["تطبيقنات مفيده 🥇"],
    ["بوتات مفيده 🥇", "قنوات مفيده 🥇"],
    ["روتين الثانويه 🫀", "12 نصيحه للثانويه 🫀"],
    ["الاستفاده من اليوتيوب 🫀"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

stream_menu = [
    ["🌙 أزهر", "☀️ عام"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

azhar_main_menu = [
    ["📖 المواد العربية 🖤", "📕 المواد الشرعية 🖤"],
    ["📘 المواد الثقافية 🖤"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

azhar_sharia_menu = [
    ["تفسير... 🖤", "حديث... 🖤"],
    ["توحيد... 🖤", "ميراث... 🖤"],
    ["فقه حنفي... 🖤", "فقه مالكي... 🖤"],
    ["فقه شافعي... 🖤"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

azhar_arabic_menu = [
    ["نحو... 🖤", "صرف... 🖤"],
    ["بلاغه... 🖤", "أدب ونصوص... 🖤"],
    ["المطالعة والإنشاء... 🖤"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

material_sources_menu = [
    ["كتاب المدرسة... 🖤📖"],
    ["مذكرات... 🖤📄", "كتب خارجية... 🖤📚"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

external_books_list = [
    ["المرشد 🖤", "سلاح الأزهري 🖤"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

inheritance_external_books = [
    ["سلاح الأزهري 🖤"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

hanafi_external_books = [
    ["سلاح الأزهري 🖤"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

arabic_external_books = [
    ["المرشد 🖤", "الإمام 🖤"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

adab_external_books = [
    ["المرشد 🖤", "سلاح الأزهري 🖤"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

mutalaa_external_books = [
    ["كتاب المدرسة فقط 🖤"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

azhar_science_cultural = [
    ["أحياء... 🦠", "جيولوجيا... 🌍"],
    ["فيزياء... 💡", "كيمياء... 🧪"],
    ["إنجليزي... 🔤", "رياضيات... 🧠"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

azhar_arts_cultural = [
    ["تاريخ... 🏛️", "جغرافيا... 🗺"],
    ["فلسفة ومنطق... 🏛️", "علم نفس واجتماع... 🧠"],
    ["فرنساوي... 🥖", "إنجليزي... 🔤"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

general_science_menu = [
    ["📖 اللغة العربية", "📖 اللغة الإنجليزية"],
    ["📖 اللغة الفرنسية", "📖 اللغة الألمانية", "📖 اللغة الإيطالية"],
    ["📖 اللغة الإسبانية", "📖 اللغة الصينية"],
    ["🔬 علمي علوم", "🔬 علمي رياضة"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

general_arts_menu = [
    ["التاريخ", "الجغرافيا"],
    ["الإحصاء", "علم نفس واجتماع"],
    ["فلسفة ومنطق", "فرنساوي"],
    ["🔙 رجوع", "🏠 رجوع إلى البداية"]
]

sharia_subjects = ["تفسير... 🖤", "حديث... 🖤", "توحيد... 🖤", "ميراث... 🖤", "فقه حنفي... 🖤", "فقه مالكي... 🖤", "فقه شافعي... 🖤"]
arabic_subjects = ["نحو... 🖤", "صرف... 🖤", "بلاغه... 🖤", "أدب ونصوص... 🖤", "المطالعة والإنشاء... 🖤"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    reply_markup = ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    await update.message.reply_text(
        "أهلاً بك يا بطل في بوت الثانوية العامة والأزهرية 🎓\nاختر من الأزرار بالأسفل:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_data = context.user_data
    current_state = user_data.get('menu_state')

    if text == "🏠 رجوع إلى البداية" or text == "القائمة الرئيسية 🔝":
        user_data.clear()
        await start(update, context)
        return

    # الأزرار الرئيسية للبوت
    if text == "بحث عن كتاب 🔍":
        await update.message.reply_text("🔍 **بحث عن كتاب:**\nأرسل اسم الكتاب أو المادة التي تبحث عنها وسأساعدك في إيجادها يا بطل ✨")
        return
    elif text == "المكتبة 📚🌱":
        user_data['menu_state'] = 'library'
        reply_markup = ReplyKeyboardMarkup(library_menu, resize_keyboard=True)
        await update.message.reply_text("📚 **المكتبة العامة:**\nمرحباً بك في عالم الكتب والقراءة، اختر القسم الذي تفضله للتصفح 🌟", reply_markup=reply_markup)
        return
    elif text == "أضف كتاب 📥📕":
        await update.message.reply_text("📥 **أضف كتاب:**\nشكراً لمساهمتك معنا يا بطل! أرسل ملف الكتاب أو تفاصيله ليتم إضافته للمكتبة قريباً 💙")
        return
    elif text == "اطلب كتاب 🔍📕":
        await update.message.reply_text("🔍 **اطلب كتاب:**\nاكتب اسم الكتاب أو المذكرة التي تحتاجها وسنقوم بتوفيرها لك في أسرع وقت ممكن 🚀")
        return

    # التنقل داخل أقسام المكتبة
    if current_state == 'library':
        if text == "🔙 رجوع":
            user_data.clear()
            await start(update, context)
            return
        elif text == "| كُتُبٌ مُنَوَّعَةٌ | 💛🤎":
            user_data['menu_state'] = 'diverse_books'
            reply_markup = ReplyKeyboardMarkup(diverse_books_menu, resize_keyboard=True)
            await update.message.reply_text("💛 **قسم كتب منوعة (الصفحة 1):**\nاختر الكتاب أو الرواية التي تريد قراءتها 📚✨", reply_markup=reply_markup)
            return
        elif text == "| الرُّوايات | 💌❤️":
            user_data['menu_state'] = 'novels'
            reply_markup = ReplyKeyboardMarkup(novels_menu, resize_keyboard=True)
            await update.message.reply_text("💌 **قسم الروايات:**\nاختر الرواية التي تفضلها 📚✨", reply_markup=reply_markup)
            return
        elif text == "| النُّصُوصُ وَالْخَوَاطِرُ | 🍿":
            user_data['menu_state'] = 'texts'
            reply_markup = ReplyKeyboardMarkup(texts_menu, resize_keyboard=True)
            await update.message.reply_text("🍿 **قسم النصوص والخواطر:**\nاختر ما يناسب ذوقك الأدبي 📖✨", reply_markup=reply_markup)
            return
        elif text == "| الْمَكْتَبَةُ الْإِسْلَامِيَّةُ | 🕋":
            user_data['menu_state'] = 'islamic_library'
            reply_markup = ReplyKeyboardMarkup(islamic_library_menu, resize_keyboard=True)
            await update.message.reply_text("🕋 **المكتبة الإسلامية:**\nاختر القسم المطلوب لتصفح الكتب والدراسات الإسلامية 🌟", reply_markup=reply_markup)
            return
        elif text == "| اَلْأَدَبُ وَالشِّعْرُ | 📜🤎":
            user_data['menu_state'] = 'literature_poetry'
            reply_markup = ReplyKeyboardMarkup(literature_poetry_menu, resize_keyboard=True)
            await update.message.reply_text("📜 **قسم الأدب والشعر:**\nاختر الديوان أو الشاعر المفضل لديك 🌟", reply_markup=reply_markup)
            return
        elif text == "| كُتُبٌ الْمَرْأَةِ | 👗":
            user_data['menu_state'] = 'womens_books'
            reply_markup = ReplyKeyboardMarkup(womens_books_menu, resize_keyboard=True)
            await update.message.reply_text("👗 **قسم كتب المرأة:**\nاختر القسم المطلوب 🌟", reply_markup=reply_markup)
            return
        elif text in ["أعمال أدهم شرقاوي 📚", "رسالة لك | 🌱🤎|", "| كتاب في دقائق |.. 📖✨"]:
            await update.message.reply_text(f"لقد اخترت قسم ({text}) 🌟\n(جاري إرفاق الكتب والمحتوى الخاص بهذا القسم قريباً يا بطل ✨)")
            return

    # التنقل داخل قسم الروايات
    if current_state == 'novels':
        if text == "🔙 رجوع" or text == "القائمة الرئيسية 🔝":
            user_data['menu_state'] = 'library'
            reply_markup = ReplyKeyboardMarkup(library_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع لقائمة المكتبة:", reply_markup=reply_markup)
            return
        else:
            await update.message.reply_text(f"لقد اخترت رواية ({text}) 📖✨\n(جاري إرفاق ملف الـ PDF الخاص بالرواية قريباً يا بطل 🚀)")
            return

    # التنقل داخل قسم النصوص والخواطر
    if current_state == 'texts':
        if text == "🔙 رجوع" or text == "القائمة الرئيسية 🔝":
            user_data['menu_state'] = 'library'
            reply_markup = ReplyKeyboardMarkup(library_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع لقائمة المكتبة:", reply_markup=reply_markup)
            return
        else:
            await update.message.reply_text(f"لقد اخترت ({text}) 📖✨\n(جاري إرفاق المحتوى قريباً يا بطل 🚀)")
            return

    # التنقل داخل المكتبة الإسلامية الرئيسية
    if current_state == 'islamic_library':
        if text == "🔙 رجوع" or text == "القائمة الرئيسية 🔝":
            user_data['menu_state'] = 'library'
            reply_markup = ReplyKeyboardMarkup(library_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع لقائمة المكتبة:", reply_markup=reply_markup)
            return
        elif text == "تفسير القرآن الكريم 📖":
            user_data['menu_state'] = 'quran_tafsir'
            reply_markup = ReplyKeyboardMarkup(quran_tafsir_menu, resize_keyboard=True)
            await update.message.reply_text("📖 **تفسير القرآن الكريم:**\nاختر المفسر أو العالم المطلوب:", reply_markup=reply_markup)
            return
        elif text == "| كُتُبٌ إِسْلَامِيَّةٌ | 🕋":
            user_data['menu_state'] = 'islamic_books'
            reply_markup = ReplyKeyboardMarkup(islamic_books_menu, resize_keyboard=True)
            await update.message.reply_text("🕋 **كتب إسلامية:**\nاختر الكتاب المطلوب:", reply_markup=reply_markup)
            return

    # التعامل مع قائمة كتب إسلامية
    if current_state == 'islamic_books':
        if text == "🔙 رجوع" or text == "القائمة الرئيسية 🔝":
            user_data['menu_state'] = 'islamic_library'
            reply_markup = ReplyKeyboardMarkup(islamic_library_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع للمكتبة الإسلامية:", reply_markup=reply_markup)
            return
        else:
            await update.message.reply_text(f"لقد اخترت كتاب ({text}) 📖✨\n(جاري إرفاق ملف الكتاب قريباً يا بطل 🚀)")
            return

    # التعامل مع قائمة تفسير القرآن الكريم
    if current_state == 'quran_tafsir':
        if text == "🔙 رجوع" or text == "القائمة الرئيسية 🔝":
            user_data['menu_state'] = 'islamic_library'
            reply_markup = ReplyKeyboardMarkup(islamic_library_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع للمكتبة الإسلامية:", reply_markup=reply_markup)
            return
        else:
            await update.message.reply_text(f"لقد اخترت تفاسير الشيخ/العالم ({text}) 📖✨\n(جاري إرفاق الكتب والمحتوى قريباً يا بطل 🚀)")
            return

    # التعامل مع قائمة الأدب والشعر
    if current_state == 'literature_poetry':
        if text == "🔙 رجوع" or text == "القائمة الرئيسية 🔝":
            user_data['menu_state'] = 'library'
            reply_markup = ReplyKeyboardMarkup(library_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع لقائمة المكتبة:", reply_markup=reply_markup)
            return
        else:
            await update.message.reply_text(f"لقد اخترت ({text}) 📜✨\n(جاري إرفاق المحتوى قريباً يا بطل 🚀)")
            return

    # التعامل مع قائمة كتب المرأة
    if current_state == 'womens_books':
        if text == "🔙 رجوع" or text == "القائمة الرئيسية 🔝":
            user_data['menu_state'] = 'library'
            reply_markup = ReplyKeyboardMarkup(library_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع لقائمة المكتبة:", reply_markup=reply_markup)
            return
        else:
            await update.message.reply_text(f"لقد اخترت ({text}) 👗✨\n(جاري إرفاق المحتوى قريباً يا بطل 🚀)")
            return

    # التعامل مع قائمة كتب منوعة (الصفحة الأولى)
    if current_state == 'diverse_books':
        if text == "🔙 رجوع":
            user_data['menu_state'] = 'library'
            reply_markup = ReplyKeyboardMarkup(library_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع لقائمة المكتبة:", reply_markup=reply_markup)
            return
        elif text == "| المزيد من الكتب المنوعة | ⭐":
            user_data['menu_state'] = 'diverse_books_p2'
            reply_markup = ReplyKeyboardMarkup(diverse_books_page2, resize_keyboard=True)
            await update.message.reply_text("⭐ **قسم كتب منوعة (الصفحة الثانية):**\nالمزيد من الكتب الرائعة لتختر منها 📚✨", reply_markup=reply_markup)
            return
        else:
            await update.message.reply_text(f"لقد اخترت كتاب ({text}) 📖✨\n(جاري إرفاق ملف الـ PDF الخاص بالكتاب قريباً يا بطل 🚀)")
            return

    # التعامل مع قائمة كتب منوعة (الصفحة الثانية)
    if current_state == 'diverse_books_p2':
        if text == "🔙 رجوع":
            user_data['menu_state'] = 'diverse_books'
            reply_markup = ReplyKeyboardMarkup(diverse_books_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع للصفحة الأولى من كتب منوعة:", reply_markup=reply_markup)
            return
        else:
            await update.message.reply_text(f"لقد اخترت كتاب ({text}) 📖✨\n(جاري إرفاق ملف الـ PDF الخاص بالكتاب قريباً يا بطل 🚀)")
            return

    if text == "منوعات... 🎁":
        user_data['menu_state'] = 'variety'
        reply_markup = ReplyKeyboardMarkup(variety_menu, resize_keyboard=True)
        await update.message.reply_text("أهلاً بك في قسم المنوعات والملفات العامة 🎁✨\nاختر ما يناسبك:", reply_markup=reply_markup)
        return

    if text in ["بوكليتات 2024 🔥", "بوكليتات 2025 🔥"]:
        await update.message.reply_text(f"لقد اخترت ({text}) 📚🔥\n(جاري إرفاق بوكليتات الامتحانات قريباً يا بطل ✨)")
        return

    if text == "للـتـواصـل معـنا 🤝":
        await update.message.reply_text("للتواصل مع إدارة البوت أو للإبلاغ عن مشكلة، يمكنك مراسلتنا هنا: \n(ضع معرف التواصل هنا 🤝✨)")
        return

    if text == "مطور البوت ✨❤️":
        await update.message.reply_text("تم تطوير هذا البوت لمساعدة طلاب الثانوية العامة والأزهرية 💻❤️️\nمطور البوت تحت أمرك دائماً في أي استفسار ✨")
        return

    if text == "نصائح... ❤" and current_state == 'variety':
        user_data['menu_state'] = 'tips'
        reply_markup = ReplyKeyboardMarkup(tips_menu, resize_keyboard=True)
        await update.message.reply_text("قسم النصائح والإرشادات الهامة للثانوية العامة والأزهرية ❤️✨\nاختر القسم المطلوب:", reply_markup=reply_markup)
        return

    if current_state == 'tips':
        if text == "🔙 رجوع":
            user_data['menu_state'] = 'variety'
            reply_markup = ReplyKeyboardMarkup(variety_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع لقائمة المنوعات:", reply_markup=reply_markup)
            return
        elif text in [
            "مشاكل وحلها 🥇", "اسئلة واجاباتها 🥇", "نصائح للثانوية 🥇", 
            "جداول مذاكرة 🥇", "تطبيقنات مفيده 🥇", "بوتات مفيده 🥇", 
            "قنوات مفيده 🥇", "روتين الثانويه 🫀", "12 نصيحه للثانويه 🫀", 
            "الاستفاده من اليوتيوب 🫀"
        ]:
            await update.message.reply_text(f"لقد اخترت ({text}) 🚀\n(جاري إرفاق المحتوى والنصائح قريباً يا بطل ✨)")
            return

    if current_state == 'variety':
        if text == "🔙 رجوع":
            user_data.clear()
            await start(update, context)
            return
        elif text in ["تحدي الـ30 يوم 💼", "كتكوتي... 🐥", "تنسيق 2024 📊", "تنسيق 2023 📊", "تنسيق 2022 📊", "تنسيق 2021 📊", "أفضل المدرسين... ❤️"]:
            await update.message.reply_text(f"لقد اخترت ({text}) 🚀\n(جاري إرفاق المحتوى قريباً يا بطل ✨)")
            return

    if text in ["عِلْمِي... 💙", "أدبي... 🖤"]:
        branch = "🔬 علمي" if "عِلْمِي" in text else "📜 أدبي"
        user_data['branch'] = branch
        reply_markup = ReplyKeyboardMarkup(stream_menu, resize_keyboard=True)
        await update.message.reply_text(f"لقد اخترت ({text}) 🎯\nهل تريد قسم الأزهر أم العام؟", reply_markup=reply_markup)
        return

    if text in ["🌙 أزهر", "☀️ عام"]:
        user_data['system'] = text
        branch = user_data.get('branch', '')
        
        if text == "🌙 أزهر":
            reply_markup = ReplyKeyboardMarkup(azhar_main_menu, resize_keyboard=True)
            await update.message.reply_text("أهلاً بك في قسم الثانوية الأزهرية 🌙\nاختر تصنيف المواد المطلوبة:", reply_markup=reply_markup)
        else:
            if branch == "🔬 علمي":
                reply_markup = ReplyKeyboardMarkup(general_science_menu, resize_keyboard=True)
                await update.message.reply_text("مرحباً بك في قسم (علمي عام) 🧪📚\nاختر المادة أو القسم:", reply_markup=reply_markup)
            else:
                reply_markup = ReplyKeyboardMarkup(general_arts_menu, resize_keyboard=True)
                await update.message.reply_text("مرحباً بك في قسم (أدبي عام) 🏛📚\nاختر المادة المطلوبة:", reply_markup=reply_markup)
        return

    if text == "📕 المواد الشرعية 🖤":
        user_data['category'] = 'sharia'
        reply_markup = ReplyKeyboardMarkup(azhar_sharia_menu, resize_keyboard=True)
        await update.message.reply_text("قسم المواد الشرعية المشتركة للأزهر 📕:", reply_markup=reply_markup)
        return

    if text == "📖 المواد العربية 🖤":
        user_data['category'] = 'arabic'
        reply_markup = ReplyKeyboardMarkup(azhar_arabic_menu, resize_keyboard=True)
        await update.message.reply_text("قسم المواد العربية المشتركة للأزهر 📖:", reply_markup=reply_markup)
        return

    if text == "📘 المواد الثقافية 🖤":
        user_data['category'] = 'cultural'
        branch = user_data.get('branch', '')
        if branch == "🔬 علمي":
            reply_markup = ReplyKeyboardMarkup(azhar_science_cultural, resize_keyboard=True)
            await update.message.reply_text("المواد الثقافية - علمي أزهر 🔬:", reply_markup=reply_markup)
        else:
            reply_markup = ReplyKeyboardMarkup(azhar_arts_cultural, resize_keyboard=True)
            await update.message.reply_text("المواد الثقافية - أدبي أزهر 📜:", reply_markup=reply_markup)
        return

    if text in sharia_subjects or text in arabic_subjects:
        user_data['subject'] = text
        reply_markup = ReplyKeyboardMarkup(material_sources_menu, resize_keyboard=True)
        await update.message.reply_text(f"اختر مصدر المادة لـ ({text}) 📚:", reply_markup=reply_markup)
        return

    if text in ["كتاب المدرسة... 🖤📖", "مذكرات... 🖤📄", "كتب خارجية... 🖤📚"]:
        user_data['source_type'] = text
        subject = user_data.get('subject', '')

        if text == "كتب خارجية... 🖤📚":
            if subject == "ميراث... 🖤":
                reply_markup = ReplyKeyboardMarkup(inheritance_external_books, resize_keyboard=True)
            elif subject == "فقه حنفي... 🖤":
                reply_markup = ReplyKeyboardMarkup(hanafi_external_books, resize_keyboard=True)
            elif subject in ["نحو... 🖤", "صرف... 🖤", "بلاغه... 🖤"]:
                reply_markup = ReplyKeyboardMarkup(arabic_external_books, resize_keyboard=True)
            elif subject == "أدب ونصوص... 🖤":
                reply_markup = ReplyKeyboardMarkup(adab_external_books, resize_keyboard=True)
            elif subject == "المطالعة والإنشاء... 🖤":
                reply_markup = ReplyKeyboardMarkup(mutalaa_external_books, resize_keyboard=True)
            else:
                reply_markup = ReplyKeyboardMarkup(external_books_list, resize_keyboard=True)
            await update.message.reply_text(f"اختر الكتاب الخارجي لـ ({subject}) 📚:", reply_markup=reply_markup)
        elif text == "كتاب المدرسة... 🖤📖":
            if subject == "تفسير... 🖤":
                file_id = "BQACAgQAAxkBAAPhasBfbZVSU0VZHIxSLdUuvxh-cGIAAuAgAAJlqAFSK5tZGFlmGsI9BA"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب المدرسة - تفسير**")
            elif subject == "حديث... 🖤":
                file_id = "BQACAgQAAxkBAAIBbGrAgJ_PVbOg164PM1Y9ZRXSvZq9AAIGIQACZagBUrnPU6LJUFo4PQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب المدرسة - حديث**")
            elif subject == "توحيد... 🖤":
                file_id = "BQACAgQAAxkBAAICOGrAkCybWzp3HN9e0_9ynoT5FLwiAAIUIQACZagBUr62XJA6mhmEPQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب المدرسة - توحيد**")
            elif subject == "ميراث... 🖤":
                file_id_1 = "BQACAgQAAxkBAAIDYWrAofPI96vGCaOxB7cpPKZzq-uUAAK6FAAClhwRUUlqFdFjps0gPQQ"
                file_id_2 = "BQACAgQAAxkBAAIDYmrAofO6JNoa8i9TCHB3SLTe6DgUAAJ6FgAC9JnpU99QaXHw9bHtPQQ"
                await update.message.reply_document(document=file_id_1, caption="📖 **كتاب المدرسة - ميراث (الجزء الأول)**")
                await update.message.reply_document(document=file_id_2, caption="📖 **كتاب المدرسة - ميراث (الجزء الثاني)**")
            elif subject == "نحو... 🖤":
                file_id = "BQACAgQAAxkBAAIEBWrAsX6vOEB6Q84eTqCvWVpCvfzJAALHFAAClhwRUUkZ3BEcIBxEPQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب المدرسة - نحو**")
            elif subject == "صرف... 🖤":
                file_id = "BQACAgQAAxkBAAIEC2rAswkuU_QeW7MpVzNhH9x_62vsAALvFwACjxogUf54IDTDy8Y7PQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب المدرسة - صرف**")
            elif subject == "بلاغه... 🖤":
                file_id = "BQACAgQAAxkBAAIEEWrA3K5z4GPRve0W0Lb0wPobX-TWAALwFwACjxogUcCFg5bUsYVhPQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب المدرسة - بلاغة**")
            elif subject == "أدب ونصوص... 🖤":
                file_id = "BQACAgQAAxkBAAIEF2rA3jeQrIPRD3K_ByReb0RzGiODAALFFAAClhwRUXq2UIl95OwuPQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب المدرسة - أدب ونصوص**")
            elif subject == "المطالعة والإنشاء... 🖤":
                file_id = "BQACAgQAAxkBAAIEHWrA3-xxAAGI7lwoJZloP5q6RJSH7gACxhQAApYcEVGEgLOPI3XD-z0E"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب المدرسة - المطالعة والإنشاء**")
            else:
                await update.message.reply_text(f"لقد اخترت كتاب المدرسة لـ ({subject}) ✨\n(جاري إرفاق الملف قريباً 🚀)")
        else:
            await update.message.reply_text(f"لقد اخترت ({text}) الخاصة بـ ({subject}) ✨\n(جاري إرفاق الملف قريباً 🚀)")
        return

    if text in ["المرشد 🖤", "سلاح الأزهري 🖤", "الإمام 🖤", "كتاب المدرسة فقط 🖤"]:
        subject = user_data.get('subject', '')
        
        if text == "كتاب المدرسة فقط 🖤":
            await update.message.reply_text("عفواً، هذه المادة متوفرة بكتاب المدرسة فقط ولا توجد لها كتب خارجية حالياً 📚✨")
            return

        if subject == "تفسير... 🖤":
            if text == "المرشد 🖤":
                file_id = "BQACAgQAAxkBAAIBKmrAb_RtRobEvZvry5Bm4sRUb1dhAAICIQACZagBUkgHaiwcjLyVPQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب المرشد في تفسير القرآن الكريم**\nبالتوفيق والنجاح دائماً 🌟")
            elif text == "سلاح الأزهري 🖤":
                file_id = "BQACAgQAAxkBAAIBT2rAfInBWYkBpkWSH0gDrTQkJJztAAIEIQACZagBUo0pG1sAAQveGD0E"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب سلاح الأزهري في تفسير القرآن الكريم**\nبالتوفيق والنجاح دائماً 🌟")
        elif subject == "حديث... 🖤":
            if text == "المرشد 🖤":
                file_id = "BQACAgQAAxkBAAIBb2rAgVnERs8pXwFbyMjmSFPf5kPSAAIHIQACZagBUhJOG_t2SL41PQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب المرشد في الحديث الشريف**\nبالتوفيق والنجاح دائماً 🌟")
            elif text == "سلاح الأزهري 🖤":
                file_id = "BQACAgQAAxkBAAIBcmrAgiz7R4Ecasacmy7Xo1CFSFkjAAIIIQACZagBUjlGe0tDmJGoPQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب سلاح الأزهري في الحديث الشريف**\nبالتوفيق والنجاح دائماً 🌟")
        elif subject == "توحيد... 🖤":
            if text == "المرشد 🖤":
                file_id = "BQACAgQAAxkBAAIBlmrAhfxNYabIjFY_dvkjMaeBf_WLAALUFAACS2PwUXU0csWYQh3mPQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب المرشد في التوحيد**\nبالتوفيق والنجاح دائماً 🌟")
            elif text == "سلاح الأزهري 🖤":
                file_id = "BQACAgQAAxkBAAIBl2rAhfz0glD3dzWp_DWfDWl6ODwvAALVFAACS2PwUchwDU27OkrAPQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب سلاح الأزهري في التوحيد**\nبالتوفيق والنجاح دائماً 🌟")
        elif subject == "ميراث... 🖤":
            if text == "سلاح الأزهري 🖤":
                file_id = "BQACAgQAAxkBAAIDZmrApeQ-YwXw3j15WXqFPW3GnS2jAAIUEwACV0P4UdIKiTrqx50wPQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب سلاح الأزهري في الميراث**\nبالتوفيق والنجاح دائماً 🌟")
        elif subject == "فقه حنفي... 🖤":
            if text == "سلاح الأزهري 🖤":
                file_id = "BQACAgQAAxkBAAID4mrArFuaXzBVeJGJk9kEbBGCrPThAAIzFQACIIthU4gWxkgXb19VPQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب سلاح الأزهري في الفقه الحنفي**\nبالتوفيق والنجاح دائماً 🌟")
        elif subject == "فقه مالكي... 🖤":
            if text == "المرشد 🖤":
                file_id_1 = "BQACAgQAAxkBAAID2WrAq4WSvJerDv1Dd3DoVGldl3DHAAIvFQACIIthU7hKvkIQLVvwPQQ"
                file_id_2 = "BQACAgQAAxkBAAID2mrAq4Wtad0lcJBOv73qPsI-lBtqAAJGGAACIVYRUeIOf-Fc4YMaPQQ"
                await update.message.reply_document(document=file_id_1, caption="📖 **كتاب المرشد في الفقه المالكي (الجزء الأول)**")
                await update.message.reply_document(document=file_id_2, caption="📖 **كتاب المرشد في الفقه المالكي (الجزء الثاني)**")
        elif subject == "فقه شافعي... 🖤":
            if text == "المرشد 🖤":
                file_id_1 = "BQACAgQAAxkBAAID22rAq4XV1Sd7z5lHqTC6FRH73RMtAAIwFQACIIthU7cI4XIhbR4lPQQ"
                file_id_2 = "BQACAgQAAxkBAAID3GrAq4VP6GdrGlhzAq-gwpKzuafqAAIxFQACIIthU9om_aTYpVYjPQQ"
                await update.message.reply_document(document=file_id_1, caption="📖 **كتاب المرشد في الفقه الشافعي**")
                await update.message.reply_document(document=file_id_2, caption="📖 **أسئلة المرشد في الفقه الشافعي**")
        elif subject == "نحو... 🖤":
            if text == "الإمام 🖤":
                file_id = "BQACAgQAAxkBAAIEBmrAsX5cRjeQa_-mwPnb852DL12pAAIhGAACEj3xUsNlXfLhS5j4PQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب الإمام في النحو**\nبالتوفيق والنجاح دائماً 🌟")
            elif text == "المرشد 🖤":
                file_id = "BQACAgQAAxkBAAIEB2rAsX7GmQNcOuRybKOdMGOTBUEeAAKJFgACXXoZUl3lyQQ1cVNsPQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب المرشد في النحو**\nبالتوفيق والنجاح دائماً 🌟")
        elif subject == "صرف... 🖤":
            if text == "المرشد 🖤":
                file_id = "BQACAgQAAxkBAAIEDGrAswkICvaZnTfl6ywimtMWp35OAAJSFwACsz0gUth0Az0i_qn-PQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب المرشد في الصرف**\nبالتوفيق والنجاح دائماً 🌟")
            elif text == "الإمام 🖤":
                file_id = "BQACAgIAAxkBAAIEDWrAswkb_DGG6H-HIHBsBkbKILpIAALmZAACuH3gS_TMevVNd-12PQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب الإمام في الصرف**\nبالتوفيق والنجاح دائماً 🌟")
        elif subject == "بلاغه... 🖤":
            if text == "المرشد 🖤":
                file_id = "BQACAgQAAxkBAAIEEmrA3K5eWtdEHgQzg3syjtzllq1BAAJ1FwACsz0gUugHTbx29LK8PQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب المرشد في البلاغة**\nبالتوفيق والنجاح دائماً 🌟")
            elif text == "الإمام 🖤":
                file_id = "BQACAgIAAxkBAAIEE2rA3K7Zv52MlXBwsYKlXVUyor-rAALhZAACuH3gSwHlfYWU_jpzPQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب الإمام في البلاغة**\nبالتوفيق والنجاح دائماً 🌟")
        elif subject == "أدب ونصوص... 🖤":
            if text == "المرشد 🖤":
                file_id = "BQACAgQAAxkBAAIEGGrA3jcJs39q-g6hOMnt1kfJnHCbAAKNFwACsz0gUj7i0HcaZJdXPQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب المرشد في الأدب والنصوص**\nبالتوفيق والنجاح دائماً 🌟")
            elif text == "سلاح الأزهري 🖤":
                file_id = "BQACAgQAAxkBAAIEGWrA3jdrm5fx6-cxj0ZrHfRkjq8NAAJ5FwACsz0gUgM1QjeGPd3sPQQ"
                await update.message.reply_document(document=file_id, caption="📖 **كتاب سلاح الأزهري في الأدب والنصوص**\nبالتوفيق والنجاح دائماً 🌟")
        else:
            await update.message.reply_text(f"لقد اخترت كتاب ({text}) لـ ({subject}) ✨\n(جاري ربط الملف قريباً 🚀)")
        return

    if text == "🔙 رجوع":
        if current_state in ['novels', 'texts', 'islamic_library', 'literature_poetry', 'womens_books']:
            user_data['menu_state'] = 'library'
            reply_markup = ReplyKeyboardMarkup(library_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع لقائمة المكتبة:", reply_markup=reply_markup)
            return
        elif current_state == 'diverse_books_p2':
            user_data['menu_state'] = 'diverse_books'
            reply_markup = ReplyKeyboardMarkup(diverse_books_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع للصفحة الأولى:", reply_markup=reply_markup)
            return
        elif current_state == 'diverse_books':
            user_data['menu_state'] = 'library'
            reply_markup = ReplyKeyboardMarkup(library_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع لقائمة المكتبة:", reply_markup=reply_markup)
            return
        elif current_state == 'library':
            user_data.clear()
            await start(update, context)
            return
        elif 'source_type' in user_data:
            user_data.pop('source_type', None)
            subject = user_data.get('subject')
            reply_markup = ReplyKeyboardMarkup(material_sources_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع لقائمة المصادر:", reply_markup=reply_markup)
        elif 'subject' in user_data:
            user_data.pop('subject', None)
            category = user_data.get('category')
            if category == 'sharia':
                reply_markup = ReplyKeyboardMarkup(azhar_sharia_menu, resize_keyboard=True)
            else:
                reply_markup = ReplyKeyboardMarkup(azhar_arabic_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع لقائمة المواد:", reply_markup=reply_markup)
        elif 'category' in user_data or 'system' in user_data:
            user_data.pop('category', None)
            user_data.pop('system', None)
            reply_markup = ReplyKeyboardMarkup(stream_menu, resize_keyboard=True)
            await update.message.reply_text("تم الرجوع للخلف:", reply_markup=reply_markup)
        elif 'branch' in user_data:
            user_data.clear()
            await start(update, context)
        else:
            await start(update, context)
        return

    if text in ["التاريخ", "الجغرافيا", "الإحصاء", "علم نفس واجتماع", "فلسفة ومنطق", "فرنساوي"]:
        await update.message.reply_text(f"لقد اخترت ({text}) 📚✨\n(جاري إرفاق الملفات والمراجعات قريباً 🚀)")
        return

    await update.message.reply_text(f"لقد اخترت: ({text}) ✨\n(جاري ربطه بالكتب والمذكرات قريباً 📚)")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("البوت يعمل الآن بكل الأقسام والأزرار المحدثة كاملة ومظبوطة... 🚀")
    app.run_polling()

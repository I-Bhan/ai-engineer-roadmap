# 01 — التعامل مع chunks

## Concept

`list` تجمع عناصر مرتبة، و`dict` تحفظ حقول العنصر بأسماء واضحة. نستخدم `for loop` للمرور على العناصر واحدًا واحدًا.

## AI Engineering Relevance

في RAG، غالبًا نمثل كل جزء من المستند بنصه ومصدره. يجب أن تتمكن من قراءة هذه البيانات قبل تقسيمها أو إرسالها إلى embedding model.

## Task

افتح `starter.py`. أضف كودًا يطبع كل `chunk` بالشكل التالي، وبالترتيب نفسه:

```text
contract_a.txt: The contract starts on January 1.
contract_a.txt: Either party may terminate with 30 days notice.
contract_b.txt: Payment is due within 14 days.
```

استخدم `for loop`. لا تحتاج إلى `function` أو مكتبة خارجية.

## Hints

- كل عنصر في `chunks` هو `dict`.
- يمكن قراءة قيمة حقل باستخدام اسم المفتاح، مثل `chunk["source"]`.
- إذا ظهر خطأ، اقرأ اسم الخطأ ورقم السطر وأرسله مع محاولتك.

## Review

أرسل الكود الذي كتبته أو رسالة الخطأ. سنراجع المحاولة قبل فتح مهمة جديدة.

## Completion Criteria

يظهر الأسطر الثلاثة كما في المثال، بالترتيب، دون خطأ عند التشغيل. وتستطيع شرح معنى `chunks` و`chunk` و`source` في الكود.

## SRS (Software Requirements Specification)
requirements:

- The program needs to support an isosceles triangle and an isosceles trapezoid.
- In case of 3 Points (a,b,c): |dist(a,b) - dist(a,c)| < EPS  (EPS can be assumed to be 0.001).
In case of four Points (a1, a2, b, c)
|dist(a1,b) - dist(a2,c)| < EPS
 dist(a1,a2) <= dist(b,c)
a1→b and a2→c are on the same plane 


1. מבוא (Introduction)
מטרה (Purpose): הגדרת יעדו של מסמך הדרישות
.
גבולות גזרה (Scope): תיאור תחומי האחריות של התוכנה ומה נמצא בהיקף הפרויקט
.
הגדרות ומונחים (Definitions): מילון מונחים מקצועי וראשי תיבות המשמשים במסמך
.
מקורות (References): קישורים למסמכי סף קודמים (כמו מסמך PRD או SOW)
.
2. תיאור כללי (Overall Description)
נקודת מבט על המוצר (Product perspective): כיצד המוצר משתלב בסביבה או במערכות קיימות
.
סוגי משתמשים (User classes): חלוקת המשתמשים לפי תפקידים, הרשאות ומאפיינים
.
סביבת הפעלה (Operating environment): פלטפורמות, חומרה ומערכות הפעלה נתמכות
.
אילוצים והנחות יסוד (Constraints & Assumptions): מגבלות טכנולוגיות, תקניות, ארגוניות או משפטיות
.
3. דרישות מפורטות (Specific Requirements)
זהו הליבה של המסמך, והוא מחולק ל-3 סוגים עיקריים
:
דרישות פונקציונליות (Functional requirements): ההתנהגויות והפעולות שהמערכת מספקת
.
דוגמה: REQ-12: המערכת תאפשר לספרנית לרשום השאלה של ספר עבור חבר רשום.
ממשקים חיצוניים (External interfaces): הגדרת ממשקי משתמש (UI), ממשקי חומרה, וממשקים מול מערכות תוכנה חיצוניות
.
דרישות לא-פונקציונליות (Non-functional requirements): איכויות ואילוצי המערכת כגון ביצועים, אבטחה, אמינות, זמינות ותחזוקתיות
.
דוגמה: NFR-03: זמינות המערכת תהיה 99.5% בזמן שעות הפעילות.
4. נספחים (Appendices)
תרחישי שימוש (Use Cases): פירוט האינטראקציה מנקודת מבט של המשתמש (שחקן, תנאי סף, תרחיש הצלחה מרכזי ותרחישים חלופיים)
.
מילון נתונים (Data dictionary): הגדרת מבני הנתונים והשדות במערכת
.
מטריצת עקביות ומעקב (Traceability matrix): טבלה המקשרת בין כל דרישה ב-SRS לבין רכיב העיצוב ב-SDD ותסריט הבדיקה ב-STD
.
דגשים לכתיבת דרישות איכותיות ב-SRS:
דרישה טובה ב-SRS חייבת להיות חד-משמעית, ניתנת לבדיקה (Verifiable/Testable), שלמה, עקבית ובעלת סדר עדיפויות (Prioritised)
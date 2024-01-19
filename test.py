from trankit import Pipeline

import utils




def main():
    p = Pipeline("hebrew")
    text = """"לך ברח?" – לא-יברח איש כמוני!

הלוך בלאט למדני בקרי,

גם דבר כן לא-למדה לשוני

וכקרדום כבד יפול דברי.

ואם-כחי תם לריק – לא-פשעי,

חטאתכם היא ושאו העון!

לא-מצא תחתיו סדן פטישי,

קרדומי בא בעץ ריקבון.

אין דבר! אשלים עם-גורלי:

את-כלי אקשור לחגורתי,

ושכיר היום בלי שכר פעלי

אשובה לי בלאט כשבאתי.

אל-נוי אשוב ואל-עמקיו

ואכרת ברית עם שקמי יער;

ואתם – אתם מסוס ורקב

ומחר ישא כולכם סער."""


    all = p(text)
    print(all.keys())





if __name__ == "__main__":
    main()
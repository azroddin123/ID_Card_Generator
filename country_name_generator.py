import re
from googletrans import Translator

en_coutries = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
ar_countries_list = ['أفغانستان', 'جزر آلاند', 'ألبانيا', 'الجزائر', 'ساموا الأمريكية', 'أندورا', 'أنغولا', 'أنغيلا', 'أنتاركتيكا', 'أنتيغوا وبربودا', 'الأرجنتين', 'أرمينيا', 'أروبا', 'أستراليا', 'النمسا', 'أذربيجان', 'جزر البهاما', 'البحرين', 'بنغلاديش', 'بربادوس', 'بيلاروسيا', 'بلجيكا', 'بليز', 'بنين', 'برمودا', 'بوتان', 'بوليفيا، الحالة المتعددة الجنسيات', 'بونير، سينت أوستاتيوس وسابا', 'البوسنة والهرسك', 'بوتسوانا', 'جزيرة بوجيت', 'البرازيل', 'إقليم المحيط البريطاني الهندي', 'بروناي دار السلام', 'بلغاريا', 'بوركينا فاسو', 'بوروندي', 'كمبوديا', 'الكاميرون', 'كندا', 'الرأس الأخضر', 'جزر كايمان', 'جمهورية افريقيا الوسطى', 'تشاد', 'شيلي', 'الصين', 'جزيرة الكريسماس', 'جزر كوكوس (كيلينغ)', 'كولومبيا', 'جزر القمر', 'كونغو', 'الكونغو، الجمهورية الديمقراطية', 'جزر كوك', 'كوستا ريكا', 'ساحل العاج', 'كرواتيا', 'كوبا', 'كوراساو', 'قبرص', 'جمهورية التشيك', 'الدنمارك', 'جيبوتي', 'دومينيكا', 'جمهورية الدومينيكان', 'الإكوادور', 'مصر', 'المنقذ', 'غينيا الإستوائية', 'إريتريا', 'إستونيا', 'أثيوبيا', 'جزر فوكلاند (مالفيناس)', 'جزر فاروس', 'فيجي', 'فنلندا', 'فرنسا', 'غيانا الفرنسية', 'بولينيزيا الفرنسية', 'المناطق الجنوبية لفرنسا', 'غابون', 'غامبيا', 'جورجيا', 'ألمانيا', 'غانا', 'جبل طارق', 'اليونان', 'الأرض الخضراء', 'غرينادا', 'غواديلوب', 'غوام', 'غواتيمالا', 'غيرنسي', 'غينيا', 'غينيا بيساو', 'غيانا', 'هايتي', 'قلب الجزيرة وجزر ماكدونالز', 'الكرسي الرسولي (دولة مدينة الفاتيكان)', 'هندوراس', 'هونج كونج', 'هنغاريا', 'أيسلندا', 'الهند', 'إندونيسيا', 'إيران، جمهورية إسلامية', 'العراق', 'أيرلندا', 'جزيرة آيل أوف مان', 'إسرائيل', 'إيطاليا', 'جامايكا', 'اليابان', 'جيرسي', 'الأردن', 'كازاخستان', 'كينيا', 'كيريباتي', 'كوريا، الجمهورية الشعبية الديمقراطية', 'جمهورية كوريا', 'الكويت', 'قيرغيزستان', 'جمهورية لاو الديمقراطية الشعبية', 'لاتفيا', 'لبنان', 'ليسوتو', 'ليبيريا', 'ليبيا', 'ليختنشتاين', 'ليتوانيا', 'لوكسمبورغ', 'ماكاو', 'مقدونيا، جمهورية', 'مدغشقر', 'ملاوي', 'ماليزيا', 'جزر المالديف', 'مالي', 'مالطا', 'جزر مارشال', 'مارتينيك', 'موريتانيا', 'موريشيوس', 'ضائع', 'المكسيك', 'ميكرونيزيا، ولايات ميكرون', 'جمهورية مولدوفا', 'موناكو', 'منغوليا', 'الجبل الأسود', 'مونتسيرات', 'المغرب', 'موزمبيق', 'ميانمار', 'ناميبيا', 'ناورو', 'نيبال', 'هولندا', 'كاليدونيا الجديدة', 'نيوزيلاندا', 'نيكاراغوا', 'النيجر', 'نيجيريا', 'جزيرة نورفولك', 'جزر مريانا الشمالية', 'النرويج', 'سلطنة عمان', 'باكستان', 'بالاو', 'الأراضي الفلسطينية المحتلة', 'بنما', 'بابوا غينيا الجديدة', 'باراجواي', 'بيرو', 'فيلبيني', 'بيتكيرن', 'بولندا', 'البرتغال', 'بويرتو ريكو', 'دولة قطر', 'لقاء', 'رومانيا', 'الاتحاد الروسي', 'رواندا', 'سانت بارتيليمي', 'سانت هيلانة، الصعود و ترابيسان دا كونا', 'سانت كيتس ونيفيس', 'القديسة لوسيا', 'سانت مارتن (الجزء الفرنسي)', 'سانت بيير وميكلون', 'سانت فنسنت وجزر غرينادين', 'ساموا', 'سان مارينو', 'ساو تومي وبرينسيبي', 'المملكة العربية السعودية', 'السنغال', 'صربيا', 'سيشيل', 'سيرا ليون.', 'سنغافورة', 'سينت مارتن (الجزء الهولندي)', 'سلوفاكيا', 'سلوفينيا', 'جزر سليمان', 'الصومال', 'جنوب أفريقيا', 'جورجيا الجنوبية وجزر ساندويتش الجنوبية', 'إسبانيا', 'سيريلانكا', 'السودان', 'سورينام', 'جنوب السودان', 'سفالبارد وجان ماين', 'سوازيلاند', 'السويد', 'سويسرا', 'الجمهورية العربية السورية', 'تايوان، مقاطعة الصين', 'طاجيكستان', 'تنزانيا، جمهورية المملكة المتحدة', 'تايلاند', 'تيمور - ليشتي.', 'توجو', 'تونغا', 'ترينداد وتوباغو', 'تونس', 'ديك رومى', 'تركمانستان', 'جزر تركس وكايكوس', 'توفالو', 'أوغندا', 'أوكرانيا', 'الإمارات العربية المتحدة', 'المملكة المتحدة', 'الولايات المتحدة الأمريكية', 'جزر الولايات المتحدة البعيدة الصغرى', 'أوروجواي', 'أوزبكستان', 'فانواتو', 'فنزويلا، جمهورية البوليفارية', 'فيتنام', 'جزر العذراء البريطانية', 'جزر فيرجن، الولايات المتحدة', 'واليس وفوتونا', 'اليمن', 'زامبيا', 'زيمبابوي']
en_countries_list = [] 
translator = Translator()
for i in range(len(en_coutries)) :
  ar_name = translator.translate(en_coutries[i],dest="ar")
  only_latin_text = re.search('[a-zA-Z][,]', ar_name.text)
  if(only_latin_text) :
        print(f"Skipping.....{only_latin_text}")
        pass
  else :
        ar_countries_list.append(ar_name.text)
        en_countries_list.append(en_coutries[i])
        print(ar_name.text)
  
with open("./data/english_county_names.text","w") as file:
    for i in range(len(en_coutries)) :
        country ="Nationality: "+ en_coutries[i]
        file.write(f"{country}\n")
        
with open("./data/ar_county_names.text","w") as file:
    for i in range(len(ar_countries_list)) :
        ar_name = "الجنسية" + ": "+ar_countries_list[i]
        file.write(f"{ar_name}\n")

print(ar_countries_list)
print(en_countries_list)
print(len(ar_countries_list),len(en_countries_list))
# print(len(ar_countries_list))


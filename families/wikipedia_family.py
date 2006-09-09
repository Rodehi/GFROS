# -*- coding: utf-8  -*-

import urllib
import family, config

__version__ = '$Id$'

# The Wikimedia family that is known as Wikipedia, the Free Encyclopedia

class Family(family.Family):
    
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'wikipedia'

        self.langs = {
            'dk':'da.wikipedia.org',
            'jp':'ja.wikipedia.org',
            'minnan':'zh-min-nan.wikipedia.org',
            'nb':'no.wikipedia.org',
            'tokipona':'tokipona.wikipedia.org',
            'zh-cn':'zh.wikipedia.org',
            'zh-tw':'zh.wikipedia.org'
            }
        for lang in self.knownlanguages:
            self.langs[lang] = lang+'.wikipedia.org'

        # Override defaults
        self.namespaces[2]['cs'] = u'Wikipedista'
        self.namespaces[3]['cs'] = u'Wikipedista diskuse'

        # Most namespaces are inherited from family.Family.
        self.namespaces[4] = {
            '_default': [u'Wikipedia', self.namespaces[4]['_default']],
            'ar': u'ويكيبيديا',
            'ast':u'Uiquipedia',
            'az': u'Vikipediya',
            'be': u'Вікіпэдыя',
            'bg': u'Уикипедия',
            'bn': u'উইকিপেডিয়া',
            'ca': u'Viquipèdia',
            'cs': u'Wikipedie',
            'csb': u'Wiki',
            'cy': u'Wicipedia',
            'el': u'Βικιπαίδεια',
            'eo': u'Vikipedio',
            'et': u'Vikipeedia',
            'fa': u'ویکی‌پدیا',
            'fr': u'Wikipédia',
            'fur':u'Vichipedie',
            'fy': u'Wikipedy',
            'ga': u'Vicipéid',
            'gu': u'વિકિપીડિયા',
            'he': u'ויקיפדיה',
            'hi': u'विकिपीडिया',
            'hr': u'Wikipedija',
            'hu': u'Wikipédia',
            'ka': u'ვიკიპედია',
            'ko': u'위키백과',
            'ku': u'Wîkîpediya',
            'la': u'Vicipaedia',
            'mk': u'Википедија',
            'ml': u'വിക്കിപീഡിയ',
            'mt': u'Wikipedija',
            'nds-nl': u'Wikipedie',
            'nv': u'Wikiibíídiiya',
            'oc': u'Wikipèdia',
            'pa': u'ਵਿਕਿਪੀਡਿਆ',
            'rmy':u'Vikipidiya',
            'ru': u'Википедия',
            'sk': u'Wikipédia',
            'sl': u'Wikipedija',
            'sr': u'Википедија',
            'ta': [u'Wikipedia', u'விக்கிபீடியா'],  # Very strange - the localized version is not the main one
            'tg': u'Википедиа',
            'tr': u'Vikipedi',
            'uk': u'Вікіпедія',
            'ur': u'منصوبہ',
            'yi': u'װיקיפּעדיע',
        }
        
        self.namespaces[5] = {
            '_default': [u'Wikipedia talk', self.namespaces[5]['_default']],
            'ab': u'Обсуждение Wikipedia',
            'af': u'WikipediaBespreking',
            'af': u'Wikipediabespreking',
            'als': u'Wikipedia Diskussion',
            'an': u'Descusión Wikipedia',
            'ar': u'نقاش ويكيبيديا',
            'ast': u'Uiquipedia discusión',
            'av': u'Обсуждение Wikipedia',
            'ay': u'Discussion Wikipedia',
            'az': u'Vikipediya müzakirəsi',
            'ba': u'Обсуждение Wikipedia',
            'bat-smg': u'Wikipedia aptarimas',
            'be': u'Абмеркаваньне Вікіпэдыя',
            'bg': u'Уикипедия беседа',
            'bm': u'Discussion Wikipedia',
            'bn': u'উইকিপেডিয়া আলাপ',
            'br': u'Kaozeadenn Wikipedia',
            'bs': u'Razgovor s Wikipediom',
            'ca': u'Viquipèdia Discussió',
            'ce': u'Обсуждение Wikipedia',
            'cs': u'Wikipedie diskuse',
            'csb': u'Diskùsëjô Wiki',
            'cv': u'Wikipedia сӳтсе явмалли',
            'cy': u'Sgwrs Wicipedia',
            'da': u'Wikipedia diskussion',
            'de': u'Wikipedia Diskussion',
            'el': u'Βικιπαίδεια συζήτηση',
            'eo': u'Vikipedia diskuto',
            'es': u'Wikipedia Discusión',
            'et': u'Vikipeedia arutelu',
            'eu': u'Wikipedia eztabaida',
            'fa': u'بحث ویکی‌پدیا',
            'fi': u'Keskustelu Wikipediasta',
            'fo': u'Wikipedia kjak',
            'fr': u'Discussion Wikipédia',
            'fur': u'Discussion Vichipedie',
            'fy': u'Wikipedy oerlis',
            'ga': u'Plé Vicipéide',
            'gn': u'Wikipedia Discusión',
            'gu': u'વિકિપીડિયા talk',
            'he': u'שיחת ויקיפדיה',
            'hi': u'विकिपीडिया वार्ता',
            'hr': u'Razgovor Wikipedija',
            'hu': u'Wikipédia vita',
            'ia': u'Discussion Wikipedia',
            'id': u'Pembicaraan Wikipedia',
            'is': u'Wikipediaspjall',
            'it': u'Discussioni Wikipedia',
            'ja': u'Wikipedia‐ノート',
            'jv': u'Dhiskusi Wikipedia',
            'ka': u'ვიკიპედია განხილვა',
            'kn': u'Wikipedia ಚರ್ಚೆ',
            'ko': u'위키백과토론',
            'ku': u'Wîkîpediya nîqaş',
            'kv': u'Обсуждение Wikipedia',
            'la': u'Disputatio Vicipaediae',
            'li': u'Euverlik Wikipedia',
            'lt': u'Wikipedia aptarimas',
            'lv': u'Wikipedia diskusija',
            'mk': u'Разговор за Википедија',
            'ml': u'വിക്കിപീഡിയ talk',
            'ms': u'Perbualan Wikipedia',
            'mt': u'Wikipedija talk',
            'nah': u'Wikipedia Discusión',
            'nap': u'Discussioni Wikipedia',
            'nds': u'Wikipedia Diskuschoon',
            'nds-nl': u'Overleg Wikipedie',
            'nl': u'Overleg Wikipedia',
            'nn': u'Wikipedia-diskusjon',
            'no': u'Wikipedia-diskusjon',
            'nv': u"Wikiibíídiiya baa yinísht'į́",
            'oc': u'Discutida Wikipèdia',
            'os': u'Дискусси Wikipedia',
            'pa': u'ਵਿਕਿਪੀਡਿਆ ਚਰਚਾ',
            'pl': u'Dyskusja Wikipedii',
            'pms':u'Discussion ant sla Wikipedia',
            'pt': u'Wikipedia Discussão',
            'qu': u'Wikipedia Discusión',
            'rmy':u'Vikipidiyake vakyarimata',
            'ro': u'Discuţie Wikipedia',
            'ru': u'Обсуждение Википедии',
            'sc': u'Wikipedia discussioni',
            'sk': u'Diskusia k Wikipédii',
            'sl': u'Pogovor o Wikipediji',
            'sq': u'Wikipedia diskutim',
            'sr': u'Разговор о Википедији',
            'su': u'Obrolan Wikipedia',
            'sv': u'Wikipediadiskussion',
            'ta': [u'Wikipedia பேச்சு', u'விக்கிபீடியா பேச்சு'],
            'te': u'Wikipedia చర్చ',
            'tg': u'Баҳси Википедиа',
            'th': u'คุยเรื่องWikipedia',
            'tr': u'Vikipedi tartışma',
            'tt': u'Wikipedia bäxäse',
            'ty': u'Discussion Wikipedia',
            'udm': u'Wikipedia сярысь вераськон',
            'uk': u'Обговорення Вікіпедія',
            'ur': u'تبادلۂ خیال منصوبہ',
            'vec':u'Discussion Wikipedia',
            'vi': u'Thảo luận Wikipedia',
            'wa': u'Wikipedia copene',
            'xal': u'Wikipedia тускар ухалвр',
            'yi': u'װיקיפּעדיע רעדן',
        }
        
        self.namespaces[100] = {
            '_default': u'Portal',
            'ar': u'بوابة',
            'cs': u'Portál',
            'eo': u'Portalo',
            'fr': u'Portail',
            'it': u'Portale',
            'he': u'פורטל',
            'it': u'Portale',
            'ka': u'პორტალი',
            'kk': u'Портал',
            'nl': u'Portaal',
            'ru': u'Портал',
            'sk': u'Portál',
            'sr': u'Портал',
        }
        
        self.namespaces[101] = {
            '_default': u'Portal talk',
            'ar': u'نقاش البوابة',
            'ca': u'Portal Discussió',
            'cs': u'Portál diskuse',
            'da': u'Portal diskussion',
            'de': u'Portal Diskussion',
            'eo': u'Portala diskuto',
            'es': u'Portal Discusión',
            'fr': u'Discussion Portail',
            'he': u'שיחת פורטל',
            'hr': u'Razgovor o portalu',
            'id': u'Pembicaraan Portal',
            'it': u'Discussioni portale',
            'ja': u'Portal‐ノート',
            'ka': u'პორტალი განხილვა',
            'kk': u'Портал талқылауы',
            'nds':u'Portal Diskuschoon',
            'nl': u'Overleg portaal',
            'no': u'Portaldiskusjon',
            'pl': u'Dyskusja portalu',
            'pt': u'Discussão Portal',
            'ro': u'Discuţie Portal',
            'ru': u'Обсуждение портала',
            'sk': u'Diskusia k portálu',
            'sq': u'Portal diskutim',
            'sr': u'Разговор о порталу',
            'sv': u'Portaldiskussion',
            'tr': u'Portal tartışma',
        }

        self.namespaces[102] = {
            '_default': u'WikiProject',
            'ca': u'Viquiprojecte',
            'es': u'Wikiproyecto',
            'fr': u'Projet',
            'it': u'Progetto',
        }
            
        self.namespaces[103] = {
            '_default': u'WikiProject talk',
            'ca': u'Viquiprojecte Discussió',
            'es': u'Wikiproyecto Discusión',
            'fr': u'Discussion Projet',
            'it': u'Discussioni progetto',
        }
        
        self.namespaces[104] = {
            '_default': u'Reference',
            'fr': u'Référence',
            
        }
        
        self.namespaces[105] = {
            '_default': u'Reference talk',
            'fr' : u'Discussion Référence',
        }
            
        self.disambiguationTemplates = {

            '_default': [u'Disambig'],
            'af':  [u'Dubbelsinnig', u'Disambig'],
            'als': [u'Begriffsklärung', u'BKL', u'Disambig'],
            'ang': [u'Disambig'],
            'ast': [u'Dixebra'],
            'ar':  [u'Disambig', u'توضيح'],
            'be':  [u'Неадназначнасьць', u'Disambig'],
            'bg':  [u'Пояснение', u'Disambig'],
            'bs':  [u'Čvor'],
            'ca':  [u'Desambiguació', u'Disambig'],
            'cs':  [u'Rozcestník', u'Rozcestník - 2 znaky', u'Rozcestník - Příjmení',
                    u'Rozcestník - místopisné jméno', u'Disambig'],
            'cy':  [u'Anamrwysedd', u'Disambig', u'Gwahaniaethu'],
            'da':  [u'Flertydig'],
            'de':  [u'Begriffsklärung', u'Disambig'],
            'el':  [u'Disambig', u'Αποσαφ'],
            'en':  [u'Disambig', u'Disambiguation', u'LND', u'2LA', u'2LC',
                    u'2LCdisambig', u'3LC', u'4LC', u'4LA', u'TLAdisambig',
                    u'Acrocandis', u'Albumdis', u'Hndis', u'Numberdis',
                    u'Roadis', u'Geodis', u'Hurricanedis', u'Interstatedis',
                    u'Listdis', u'Townshipdis', u'Dab', u'Disambig-cleanup',
                    u'Disamb', u'2CC', u'3CC', u'Shipindex'],
            'eo':  [u'Apartigilo',u'Disambig'],
            'es':  [u'Desambiguacion', u'Desambiguación', u'Desambig', u'Disambig',u'Des'],
            'et':  [u'Täpsustuslehekülg', u'Täpsustus', u'Disambig'],
            'eu':  [u'Argipen', u'Disambig'],
            'fa':  [u'ابهام‌زدایی'],
            'fi':  [u'Täsmennyssivu', u'Disambig'],
            'fr':  [u'Homonymie'],
            'frp': [u'Homonimos'],
            'fy':  [u'Tfs',u'Neibetsjuttings'],
            'ga':  [u'Idirdhealú', u'Disambig'],
            'gl':  [u'Homónimos', u'Disambig'],
            'he':  [u'DisambiguationAfter', u'פירושונים', u'Disambig'],
            'hr':  [u'Disambig', u'Razdvojba'],
            'hu':  [u'Egyert', u'Disambig',u'Egyért'],
            'ia':  [u'Disambiguation', u'Disambig'],
            'id':  [u'Disambig'],
            'io':  [u'Homonimo', u'Disambig'],
            'is':  [u'Aðgreining', u'Disambig'],
            'it':  [u'Disambigua', u'Sigla2', u'Sigla3'],
            'ja':  [u'Aimai', u'Disambig'],
            'ka':  [u'მრავალმნიშვნელოვანი'],
            'kw':  [u'Klerheans'],
            'ko':  [u'Disambig'],
            'ku':  [u'Cudakirin'],
            'la':  [u'Discretiva'],
            'lb':  [u'Homonymie', u'Disambig'],
            'li':  [u'Verdudeliking', u'Verdudelikingpazjena'],
            'ln':  [u'Bokokani'],
            'lt':  [u'Disambig'],
            'mk':  [u'Појаснување'],
            'ms':  [u'Nyahkekaburan'],
            'mt':  [u'Diżambigwazzjoni'],
            'nds': [u'Mehrdüdig Begreep','Disambig'],
            'nds-nl': [u'Dv'],
            'nl':  [u'Dp', u'DP', u'Dp2', u'Dpintro'],
            'nn':  [u'Fleirtyding'],
            'no':  [u'Peker', u'Etternavn', u'Disambig', u'Tobokstavsforkortelse'],
            'oc':  [u'Omonimia',],
            'pl':  [u'Disambig', u'DisambRulers', u'DisambigC'],
            'pt':  [u'Desambiguação', u'Disambig'],
            'ro':  [u'Dezambiguizare', u'Disambig', u'Hndis'],
            'ru':  [u'Disambig', u'Значения'],
            'scn': [u'Disambigua', u'Disambig'],
            'simple': [u'Disambig', u'Disambiguation'],
            'sk':  [u'Disambig', u'Rozlišovacia stránka', u'Disambiguation'],
            'sl':  [u'Disambig', u'Razločitev', u'Disambig-ship'],
            'sq':  [u'Kthjellim', u'Disambig'],
            'sr':  [u'Вишезначна одредница', u'Disambig'],
            'su':  [u'Disambig'],
            'sv':  [u'Betydelselista', u'Disambig', u'Förgrening', u'Gaffel',
                    u'Efternamn', u'Gren',u'Förgreningssida',u'3LC'],
            'sw':  [u'Maana'],
            'th':  [u'แก้กำกวม', u'Disambig'],
            'tl':  [u'Paglilinaw', u'Disambig'],
            'tr':  [u'Anlam ayrım', u'Disambig'],
            'vi':  [u'Trang định hướng', u'Định hướng', u'Disambig', u'Hndis'],
            'wa':  [u'Omonimeye', u'Disambig'],
            'zh':  [u'Disambig', u'消歧义', u'消歧义页', u'消歧義'],
            'zh-min-nan': [u'Khu-pia̍t-ia̍h', 'KhPI', u'Disambig'],
        }

        self.disambcatname = {
            'af':  u'dubbelsinnig',
            'als': u'Begriffsklärung',
            'ang': u'Scīrung',
            'ast': u'Dixebra',
            'ar':  u'صفحات توضيح',
            'be':  u'Вікіпэдыя:Неадназначнасьці',
            'bg':  u'Пояснителни страници',
            'ca':  u'Registre de pàginas de desambiguació',
            'cs':  u'Rozcestníky',
            'cy':  u'Gwahaniaethu',
            'da':  u'Flertdig',
            'de':  u'Begriffsklärung',
            'el':  u'Αποσαφήνιση',
            'en':  u'Disambiguation',
            'eo':  u'Apartigiloj',
            'es':  u'Desambiguación',
            'et':  u'Täpsustusleheküljed',
            'eu':  u'Argipen orriak',
            'fa':  u'صفحات ابهام‌زدایی',
            'fi':  u'Täsmennyssivu',
            'fr':  u'Homonymie',
            'fy':  u'Trochferwiisside',
            'ga':  u'Idirdhealáin',
            'gl':  u'Homónimos',
            'he':  u'פירושונים',
            'ia':  u'Disambiguation',
            'id':  u'Disambiguasi',
            'io':  u'Homonimi',
            'is':  u'Aðgreiningarsíður',
            'it':  u'Disambigua',
            'ja':  u'曖昧さ回避',
            'ka':  u'მრავალმნიშვნელოვანი',
            'kw':  u'Folennow klerheans',
            'ko':  u'동음이의어 문서',
            'ku':  u'Rûpelên cudakirinê',
            'la':  u'Discretiva',
            'lb':  u'Homonymie',
            'li':  u'Verdudelikingspazjena',
            'ln':  u'Bokokani',
            'lt':  u'Nuorodiniai straipsniai',
            'ms':  u'Nyahkekaburan',
            'mt':  u'Diżambigwazzjoni',
            'nds': u'Mehrdüdig Begreep',
            'nds-nl': u'Deurverwiespagina',
            'nl':  u'Wikipedia:Doorverwijspagina',
            'nn':  u'Fleirtydingssider',
            'no':  u'Pekere',
            'pl':  u'Strony ujednoznaczniające',
            'pt':  u'Desambiguação',
            'ro':  u'Dezambiguizare',
            'ru':  u'Многозначные термины',
            'scn': u'Disambigua',
            'sk':  u'Rozlišovacie stránky',
            'sl':  u'Razločitev',
            'sq':  u'Kthjellime',
            'sr':  u'Вишезначна одредница',
            'su':  u'Disambiguasi',
            'sv':  u'Förgreningssider',
            'th':  u'การแก้ความกำกวม',
            'tl':  u'Paglilinaw',
            'tr':  u'Anlam ayrım',
            'vi':  u'Trang định hướng',
            'wa':  u'Omonimeye',
            'zh':  u'消歧义',
            'zh-min-nan': u'Khu-pia̍t-ia̍h',
            }
        
        # On most Wikipedias page names must start with a capital letter, but some
        # languages don't use this.
            
        self.nocapitalize = ['jbo','tlh','tokipona']
            

        # on_one_line is a list of languages that want the interwiki links
        # one-after-another on a single line
        self.interwiki_on_one_line = ['hu']
        
        # A revised sorting order worked out on http://meta.wikimedia.org/wiki/Interwiki_sorting_order
        self.alphabetic_revised = ['aa','af','ak','als','am','ang','ab','ar',
            'an','roa-rup','frp','as','ast','gn','av','ay','az','id','ms','bm',
            'bn','zh-min-nan','ban','map-bms','jv','su','bug','ba','be','bh',
            'mt','bi','bo','bs','br','bg','ca','ceb','cv','cs','ch','ny','sn',
            'tum','cho','co','za','cy','da','pdc','de','dv','nv','dz','mh','et',
            'na','el','en','es','eo','eu','ee','to','fa','fo','fr','fy','ff',
            'fur','ga','gv','sm','gd','gl','gay','ki','gu','got','ko','ha','haw',
            'hy','hi','ho','hr','io','ig','ia','ie','iu','ik','os','xh','zu',
            'is','it','he','kl','xal','kn','kr','ka','ks','csb','kw','rw','ky',
            'rn','sw','kv','kg','ht','kj','ku','lad','lo','la','lv','lb','lt',
            'li','ln','jbo','lg','lmo','hu','mk','mg','ml','mi','mr','chm','mo',
            'mn','mus','my','nah','fj','nap','nds-nl','nl','cr','ne','ja','ce',
            'pih','no','nn','nrm','oc','or','om','ng','hz','ug','uz','pa','kk',
            'pi','pam','pap','ps','km','pms','nds','pl','pt','ty','ksh','ro',
            'rm','rmy','qu','ru','se','sa','sg','sc','sco','st','tn','sq','scn',
            'si','simple','sd','ss','sk','sl','so','sr','sh','fi','sv','tl',
            'ta','tt','te','tet','th','vi','ti','tlh','tg','tpi','chr','chy',
            've','tr','tk','tw','udm','uk','ur','vec','vo','fiu-vro','wa','war',
            'vls','wo','ts','ii','yi','yo','zh-yue','bat-smg','zh','zh-tw','zh-cn']

        # A sorting order for lb.wikipedia worked out by http://lb.wikipedia.org/wiki/User_talk:Otets
        self.alphabetic_lb = ['aa', 'af', 'ak', 'als', 'am', 'ang', 'ab', 'ar',
            'an', 'roa-rup', 'frp', 'as', 'ast', 'gn', 'av', 'ay', 'az', 'id', 'ms', 'bm',
            'bn', 'zh-min-nan', 'ban', 'map-bms', 'jv', 'su', 'bug', 'ba', 'be', 'bh', 'mt',
            'bi', 'bo', 'bs', 'br', 'bg', 'ca', 'ceb', 'cs', 'ch', 'chr', 'chy',
            'ny', 'sn', 'tum', 've', 'cho', 'co', 'za', 'cy', 'da', 'pdc', 'de', 'dv',
            'nv', 'dz', 'mh', 'na', 'el', 'en', 'es', 'eo', 'et', 'eu', 'ee', 'to',
            'fa', 'fo', 'fr', 'fy', 'ff', 'fur', 'ga', 'gv', 'sm', 'gd', 'gl',
            'gay', 'ki', 'gu', 'got', 'ha', 'haw', 'hy', 'he', 'hi', 'ho',
            'hr', 'io', 'ig', 'ilo', 'ia', 'ie', 'iu', 'ik', 'os', 'xh', 'zu', 'is', 'it',
            'ja', 'kl', 'xal', 'kn', 'kr', 'ka', 'ks', 'csb', 'kw', 'rw', 'ky', 'rn', 'sw',
            'kv', 'kg', 'ko', 'ht', 'kj', 'ku', 'lad', 'lo', 'la', 'lv', 'lb', 'lt', 'li',
            'ln', 'jbo', 'lg', 'lmo', 'hu', 'mk', 'mg', 'ml', 'mi', 'mr', 'chm',
            'mo', 'mn', 'mus', 'my', 'nah', 'fj', 'nap', 'nds-nl', 'nl', 'cr', 'ne', 'ce',
            'pih', 'no', 'nn', 'nrm', 'oc', 'or', 'om', 'ng', 'hz', 'ug', 'uz', 'pa', 'kk',
            'pi', 'pam', 'pap', 'ps', 'km', 'pms', 'nds', 'pl', 'pt', 'ty', 'ksh', 'ro', 'rmy', 'rm', 'qu',
            'ru', 'war', 'se', 'sa', 'sg', 'sc', 'sco', 'st', 'tn', 'sq', 'scn', 'si',
            'simple', 'sd', 'ss', 'sk', 'sl', 'so', 'sr', 'sh', 'fi', 'sv', 'tl',
            'ta', 'tt', 'te', 'tet', 'th', 'vi', 'ti', 'tlh', 'tg', 'tpi', 'cv', 'tr',
            'tk', 'tw', 'udm', 'uk', 'ur', 'vec', 'vo', 'fiu-vro', 'wa', 'vls',
            'wo', 'ts', 'ii', 'yi', 'yo', 'zh-yue', 'map-bsg', 'zh', 'zh-tw', 'zh-cn']


        # Which languages have a special order for putting interlanguage links,
        # and what order is it? If a language is not in interwiki_putfirst,
        # alphabetical order on language code is used. For languages that are in
        # interwiki_putfirst, interwiki_putfirst is checked first, and
        # languages are put in the order given there. All other languages are put
        # after those, in code-alphabetical order.
        
           
        self.interwiki_putfirst = {
            'en': self.alphabetic,
            'et': self.alphabetic_revised,
            'fi': self.alphabetic_revised,
            'fy': # alphabetic by code, but 'y' is alphabetized as 'i'
            ['aa','ab','af','ak','als','am','an','ang','ar','arc','as','ast',
             'av','ay','az','bm','bn','ba','bat-smg','be','bg','bh','bi','bo',
             'br','bs','bug','ca','ce','ceb','ch','cho','chy','chr','co','cr',
             'cs','csb','cv','cy','da','de','dv','dz','ee','el','en','eo','es',
             'et','eu','fa','ff','fi','fy','fiu-vro','fj','fo','fr','frp',
             'fur','ga','gd','gl','gn','got','gu','gv','got','xal','ko','ha',
             'haw','he','hi','hy','ho','hr','ht','hu','hz','ia','id','ie',
             'ig','ii','yi','ik','ilo','io','yo','is','it','iu','ja','jbo','jv','ka','kg',
             'ki','ky','kj','kk','kl','km','kn','kr','ks','ksh','ku','kv',
             'kw','la','lad','lb','lg','lij','li','lmo','ln','lo','lt','lv',
             'map-bms','mg','mh','mi','mk','ml','mn','mo','mr','ms','mt','mi',
             'mus','my','na','nah','nap','nds','nds-nl','ne','ng','ny','nl',
             'nn','no','nrm','nv','oc','om','or','os','pa','pam','pap','pdc',
             'pih','pl','ps','pt','qu','rmy','rm','rn','ro','roa-rup','ru',
             'rw','sa','sc','scn','sco','sd','se','sg','sh','si','simple','sk',
             'sl','sm','sn','so','sq','sr','ss','st','su','sv','sw','ta','te',
             'tet','tg','th','ti','ty','tk','tl','tn','to','tpi','tr','ts','tt',
             'tum','tw','udm','ug','uk','ur','uz','ve','vec','vi','vls','vo',
             'wa','war','ts','xh','za','zh','zh-cn','zh-min-nan','zh-tw',
             'zh-yue','zu',],
            'he': ['en'],
            'hu': ['en'],
            'lb': self.alphabetic_lb,
            'nn': ['no','nb','sv','da'] + self.alphabetic,
            'no': self.alphabetic,
            'pl': self.alphabetic,
            'simple': self.alphabetic,
            'vi': self.alphabetic_revised
            }

        self.obsolete = {'dk':'da',
                    'minnan':'zh-min-nan',
                    'nb':'no',
                    'jp':'ja',
                    'tokipona':'none',
                    'zh-tw':'zh',
                    'zh-cn':'zh'}
            
        # Language codes of the largest wikis. They should be roughly sorted
        # by size.
        # Note: currently they have been sorted by size, but with languages
        # not in the Latin alphabet counted 1/3 lower
        
        self.languages_by_size = [
            'en','de','fr','pl','nl','it','sv','pt','ja','es',
            'fi','no','ru','zh','eo','sk','da','cs','hu','ca',
            'ro','sl','id','tr','lt','he','sr','et','hr','bg',
            'uk','ko','gl','nn','ms','io','eu','nap','is','ar',
            'bs','simple','lb','vi','th','fa','sq','el','br','wa',
            'ka','ht','la','bn','sh','scn','af','ku','ast','mk',
            'lv','cy','co','tl','ksh','te','an','tt','oc','ga',
            'vec','gd','az','mr','uz','ia','be','nsd','cv','ta',
            'fy','als','li','kn','jv','lmo','fo','zh-min-nan','sw','ilo',
            'ur','su','frp','hy','sco','war','yi','pms','nrm','ceb',
            'pam','tg','fur','nds-sl','kw','hi','os','se','ug','map-bms',
            'lad','csb','pdc','ang','zh-yue','lij','ml','mt','vls','vo',
            'fiu-vro','mi','sa','ps','bat-smg','jbo','qu','am','tpi','ky',
            'mo','ie','na','wo','nah','ln','ks','rm','mn','mg',
            'bo','tet','sc','my','udm','kg','gu','gv','bm','tk',
            'kk','dv','got','roa-rup','av','ne','si','ba','chr','sm',
            'my','nv','yo',]

        # other groups of language that we might want to do at once
            
        self.cyrilliclangs = [
            'ab', 'ba', 'be', 'bg', 'ce', 'cv', 'kk', 'kv', 'ky', 'mk',
            'mn', 'mo', 'os', 'ru', 'sr', 'tg', 'tk', 'udm', 'uk', 'xal'] # languages in Cyrillic
        
        # Languages that used to be coded in iso-8859-1
        self.latin1old = ['de', 'en', 'et', 'es', 'ia', 'la', 'af', 'cs',
                    'fr', 'pt', 'sl', 'bs', 'fy', 'vi', 'lt', 'fi', 'it',
                    'no', 'simple', 'gl', 'eu', 'nds', 'co', 'mi', 'mr',
                    'id', 'lv', 'sw', 'tt', 'uk', 'vo', 'ga', 'na', 'es',
                    'nl', 'da', 'dk', 'sv', 'test']
                    
        self.mainpages = {
            'aa' :            u'Main Page',
            'ab' :            u'Main Page',
            'af' :            u'Tuisblad',
            'ak' :            u'Main Page',
            'als':            u'Houptsyte',
            'am' :            u'ዋናው ገጽ',
            'an' :            u'Portalada',
            'ang':            u'Héafodsíde',
            'ar' :            u'الصفحة الرئيسية',
            'arc':            u'Main Page',
            'as' :            u'Main Page',
            'ast':            u'Portada',
            'av' :            u'Main Page',
            'ay' :            u'Main Page',
            'az' :            u'Main Page',
            'ba' :            u'Баш бит',
            'be' :            u'Галоўная старонка',
            'bg' :            u'Начална страница',
            'bh' :            u'Main Page',
            'bi' :            u'Main Page',
            'bm' :            u'Nyɛ fɔlɔ',
            'bn' :            u'প্রধান পাতা',
            'bo' :            u'Main Page',
            'br' :            u'Main Page',
            'bs' :            u'Početna strana',
            'ca' :            u'Portada',
            'ce' :            u'Main Page',
            'ceb':            u'Main Page',
            'ch' :            u'Main Page',
            'cho':            u'Main Page',
            'chr':            u'Main Page',
            'chy':            u'Main Page',
            'co' :            u'Main Page',
            'cr' :            u'Main Page',
            'cs' :            u'Hlavní strana',
            'csb':            u'Przédnô starna',
            'cv' :            u'Тĕп страницă',
            'cy' :            u'Hafan',
            'da' :            u'Forside',
            'de' :            u'Hauptseite',
            'dv' :            u'Main Page',
            'dz' :            u'Main Page',
            'ee' :            u'Main Page',
            'el' :            u'Κύρια Σελίδα',
            'en' :            u'Main Page',
            'eo' :            u'Ĉefpaĝo',
            'es' :            u'Portada',
            'et' :            u'Esileht',
            'eu' :            u'Azala',
            'fa' :            u'صفحه‌ی اصلی',
            'ff' :            u'Hello jaɓɓorgo',
            'fi' :            u'Etusivu',
            'fiu-vro':        u'Pääleht',
            'fj' :            u'Main Page',
            'fo' :            u'Forsíða',
            'fr' :            u'Accueil',
            'fur':            u'Pagjine principâl',
            'fy' :            u'Haadside',
            'ga' :            u'Príomhleathanach',
            'gd' :            u'Duille Mòr',
            'gl' :            u'Portada',
            'gn' :            u'Main Page',
            'got':            u'Main Page',
            'gu' :            u'મુખપૃષ્ઠ',
            'gv' :            u'Main Page',
            'ha' :            u'Main Page',
            'haw':            u'Main Page',
            'he' :            u'עמוד ראשי',
            'hi' :            u'मुख्य पृष्ठ',
            'ho' :            u'Main Page',
            'hr' :            u'Glavna stranica',
            'ht' :            u'Main Page',
            'hu' :            u'Kezdőlap',
            'hy' :            u'Գլխավոր Էջ',
            'hz' :            u'Main Page',
            'ia' :            u'Wikipedia:Frontispicio',
            'id' :            u'Halaman Utama',
            'ie' :            u'Principal págine',
            'ig' :            u'Main Page',
            'ii' :            u'Main Page',
            'ik' :            u'Main Page',
            'io' :            u'Frontispico',
            'is' :            u'Forsíða',
            'it' :            u'Pagina principale',
            'iu' :            u'Main Page',
            'ja' :            u'メインページ',
            'jbo':            u'ralju ckupau',
            'jv' :            u'Kaca Utama',
            'ka' :            u'მთავარი გვერდი',
            'kg' :            u'Main Page',
            'ki' :            u'Main Page',
            'kj' :            u'Main Page',
            'kk' :            u'Main Page',
            'kl' :            u'Main Page',
            'km' :            u'Main Page',
            'kn' :            u'ಮುಖ್ಯ ಪುಟ',
            'ko' :            u'대문',
            'kr' :            u'Main Page',
            'ks' :            u'Main Page',
            'ku' :            u'Serûpel',
            'kv' :            u'Main Page',
            'kw' :            u'Main Page',
            'ky' :            u'Main Page',
            'la' :            u'Pagina prima',
            'lb' :            u'Haaptsäit',
            'lg' :            u'Main Page',
            'li' :            u'Huidpazjena',
            'ln' :            u'Lonkásá ya liboso',
            'lo' :            u'Main Page',
            'lt' :            u'Pradžia',
            'lv' :            u'Sākumlapa',
            'mg' :            u'Fandraisana',
            'mh' :            u'Main Page',
            'mi' :            u'Hau Kāinga',
            'mk' :            u'Почетна страна',
            'ml' :            u'Main Page',
            'mn' :            u'Main Page',
            'mo' :            u'Main Page',
            'mr' :            u'मुखपृष्ठ',
            'ms' :            u'Laman Utama',
            'mt' :            u'Paġna prinċipali',
            'mus':            u'Main Page',
            'my' :            u'ဗဟုိစာမ္ယက္‌န္ဟာ',
            'na' :            u'Etang õgõg',
            'nah':            u'Main Page',
            'nds':            u'Hööftsiet',
            'nds-nl':         u'Heufdpagina',
            'ne' :            u'Main Page',
            'ng' :            u'Main Page',
            'nl' :            u'Hoofdpagina',
            'nn' :            u'Hovudside',
            'no' :            u'Hovedside',
            'nv' :            u'Íiyisíí Naaltsoos',
            'ny' :            u'Main Page',
            'oc' :            u'Acuèlh',
            'om' :            u'Main Page',
            'or' :            u'Main Page',
            'os' :            u'Сæйраг фарс',
            'pa' :            u'ਮੁੱਖ ਪੰਨਾ',
            'pam':            u'Main Page',
            'pi' :            u'Main Page',
            'pl' :            u'Strona główna',
            'ps' :            u'Main Page',
            'pt' :            u'Página principal',
            'qu' :            u'Qhapaq panka',
            'rm' :            u'Main Page',
            'rn' :            u'Main Page',
            'ro' :            u'Pagina principală',
            'roa-rup':        u'Main Page',
            'ru' :            u'Заглавная страница',
            'rw' :            u'Main Page',
            'sa' :            u'मुखपृष्ठं',
            'sc' :            u'Pàzina printzipale',
            'scn':            u'Paggina principali',
            'sco':            u'Main Page',
            'sd' :            u'Main Page',
            'se' :            u'Váldosiidu',
            'sg' :            u'Main Page',
            'sh' :            u'Glavna stranica / Главна страница',
            'si' :            u'Main Page',
            'simple':         u'Main Page',
            'sk' :            u'Hlavná stránka',
            'sl' :            u'Glavna stran',
            'sm' :            u'Main Page',
            'sn' :            u'Main Page',
            'so' :            u'Main Page',
            'sq' :            u'Faqja Kryesore',
            'sr' :            u'Главна страна',
            'ss' :            u'Main Page',
            'st' :            u'Main Page',
            'su' :            u'Tepas',
            'sv' :            u'Huvudsida',
            'sw' :            u'Mwanzo',
            'ta' :            u'முதற் பக்கம்',
            'te' :            u'మొదటి పేజీ',
            'tg' :            u'Main Page',
            'th' :            u'หน้าหลัก',
            'ti' :            u'Main Page',
            'tk' :            u'Main Page',
            'tl' :            u'Unang Pahina',
            'tn' :            u'Main Page',
            'to' :            u'Main Page',
            'tpi':            u'Main Page',
            'tr' :            u'Ana Sayfa',
            'ts' :            u'Main Page',
            'tt' :            u'Täwge Bit',
            'tum':            u'Main Page',
            'tw' :            u'Main Page',
            'ty' :            u'Main Page',
            'ug' :            u'Main Page',
            'uk' :            u'Головна стаття',
            'ur' :            u'صفحہ اول',
            'uz' :            u'Main Page',
            've' :            u'Main Page',
            'vi' :            u'Trang Chính',
            'vo' :            u'Cifapad',
            'wa' :            u'Mwaisse pådje',
            'wo' :            u'Main Page',
            'xh' :            u'Main Page',
            'yi' :            u'ערשטע זײַט',
            'yo' :            u'Main Page',
            'za' :            u'Main Page',
            'zh' :            u'首页',
            'zh-min-nan':     u'Thâu-ia̍h',
            'zu' :            u'Main Page',
        }

    def version(self, code):
        return "1.8alpha"
    
    def dbName(self, code):
        # returns the name of the MySQL database
        # for historic reasons, the databases are called wikixx instead of
        # wikipediaxx for Wikipedias.
        return '%swiki' % code
    
    def code2encodings(self, code):
        """Return a list of historical encodings for a specific language
           wikipedia"""
        # Historic compatibility
        if code == 'pl':
            return 'utf-8', 'iso8859-2'
        if code == 'ru':
            return 'utf-8', 'iso8859-5'
        if code in self.latin1old:
            return 'utf-8', 'iso-8859-1'
        return self.code2encoding(code),

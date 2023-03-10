import re

# utf-16
class styles(object):
    def style_1(text):
        first_style = {
        'a' : '\u01DF',
        'b' : '\u026E',
        'c' : '\u0188',
        'd' : '\u0256',
        'e' : '\u025B',
        'f' : '\u0284',
        'g' : '\u0262',
        'h' : '\u0266',
        'i' : '\u0268',
        'j' : '\u029D',
        'k' : '\u04C4',
        'l' : '\u029F',
        'm' : '\u028D',
        'n' : '\u057C',
        'o' : '\u0585',
        'p' : '\u0584',
        'q' : '\u0566',
        'r' : '\u0280',
        's' : '\u0586',
        't' : '\u0236',
        'u' : '\u028A',
        'v' : '\u028B',
        'w' : '\u0561',
        'x' : '\u04FC',
        'y' : '\u028F',
        'z' : '\u0290',
        'A' : '\u01DF',
        'B' : '\u026E',
        'C' : '\u0188',
        'D' : '\u0256',
        'E' : '\u025B',
        'F' : '\u0284',
        'G' : '\u0262',
        'H' : '\u0266',
        'I' : '\u0268',
        'J' : '\u029D',
        'K' : '\u04C4',
        'L' : '\u029F',
        'M' : '\u028D',
        'N' : '\u057C',
        'O' : '\u0585',
        'P' : '\u0584',
        'Q' : '\u0566',
        'R' : '\u0280',
        'S' : '\u0586',
        'T' : '\u0236',
        'U' : '\u028A',
        'V' : '\u028B',
        'W' : '\u0561',
        'X' : '\u04FC',
        'Y' : '\u028F',
        'Z' : '\u0290'
        }
        pattern = re.compile(r'(' + '|'.join(first_style.keys()) + r')')
        result = pattern.sub(lambda x: first_style[x.group()], text)
        return(result)

    def style_2(text):
        second_style = {
        'a' : 'Ⲁ',
        'b' : 'Ⲃ',
        'c' : 'Ⲥ',
        'd' : 'Ⲇ',
        'e' : 'Ⲉ',
        'f' : '𝓕',
        'g' : '𝓖',
        'h' : 'Ⲏ',
        'i' : 'Ⲓ',
        'j' : '𝓙',
        'k' : 'Ⲕ',
        'l' : '𝓛',
        'm' : 'Ⲙ',
        'n' : 'Ⲛ',
        'o' : 'Ⲟ',
        'p' : 'Ⲣ',
        'q' : '𝓠',
        'r' : 'Ꞅ',
        's' : 'Ϩ',
        't' : 'Ⲧ',
        'u' : 'ⴑ',
        'v' : '𝓥',
        'w' : 'Ⲱ',
        'x' : 'Ⲭ',
        'y' : 'Ⲩ',
        'z' : 'Ⲍ',
        'A' : 'Ⲁ',
        'B' : 'Ⲃ',
        'C' : 'Ⲥ',
        'D' : 'Ⲇ',
        'E' : 'Ⲉ',
        'F' : '𝓕',
        'G' : '𝓖',
        'H' : 'Ⲏ',
        'I' : 'Ⲓ',
        'J' : '𝓙',
        'K' : 'Ⲕ',
        'L' : '𝓛',
        'M' : 'Ⲙ',
        'N' : 'Ⲛ',
        'O' : 'Ⲟ',
        'P' : 'Ⲣ',
        'Q' : '𝓠',
        'R' : 'Ꞅ',
        'S' : 'Ϩ',
        'T' : 'Ⲧ',
        'U' : 'ⴑ',
        'V' : '𝓥',
        'W' : 'Ⲱ',
        'X' : 'Ⲭ',
        'Y' : 'Ⲩ',
        'Z' : 'Ⲍ'
        }
        pattern = re.compile(r'(' + '|'.join(second_style.keys()) + r')')
        result = pattern.sub(lambda x: second_style[x.group()], text)
        return(result)

    def style_3(text):
        third_style = {
        'a' : 'ą',
        'b' : 'ც',
        'c' : 'ƈ',
        'd' : 'ɖ',
        'e' : 'ɛ',
        'f' : 'ʄ',
        'g' : 'ɠ',
        'h' : 'ɧ',
        'i' : 'ı',
        'j' : 'ʝ',
        'k' : 'ƙ',
        'l' : 'Ɩ',
        'm' : 'ɱ',
        'n' : 'ŋ',
        'o' : 'ơ',
        'p' : '℘',
        'q' : 'զ',
        'r' : 'ཞ',
        's' : 'ʂ',
        't' : 'ɬ',
        'u' : 'ų',
        'v' : '۷',
        'w' : 'ῳ',
        'x' : 'ҳ',
        'y' : 'ყ',
        'z' : 'ʑ',
        'A' : 'ą',
        'B' : 'ც',
        'C' : 'ƈ',
        'D' : 'ɖ',
        'E' : 'ɛ',
        'F' : 'ʄ',
        'G' : 'ɠ',
        'H' : 'ɧ',
        'I' : 'ı',
        'J' : 'ʝ',
        'K' : 'ƙ',
        'L' : 'Ɩ',
        'M' : 'ɱ',
        'N' : 'ŋ',
        'O' : 'ơ',
        'P' : '℘',
        'Q' : 'զ',
        'R' : 'ཞ',
        'S' : 'ʂ',
        'T' : 'ɬ',
        'U' : 'ų',
        'V' : '۷',
        'W' : 'ῳ',
        'X' : 'ҳ',
        'Y' : 'ყ',
        'Z' : 'ʑ'
        }
        pattern = re.compile(r'(' + '|'.join(third_style.keys()) + r')')
        result = pattern.sub(lambda x: third_style[x.group()], text)
        return(result)

    def style_4(text):
        fourth_style = {
        'a' : '🄰',
        'b' : '🄱',
        'c' : '🄲',
        'd' : '🄳',
        'e' : '🄴',
        'f' : '🄵',
        'g' : '🄶',
        'h' : '🄷',
        'i' : '🄸',
        'j' : '🄹',
        'k' : '🄺',
        'l' : '🄻',
        'm' : '🄼',
        'n' : '🄽',
        'o' : '🄾',
        'p' : '🄿',
        'q' : '🅀',
        'r' : '🅁',
        's' : '🅂',
        't' : '🅃',
        'u' : '🅄',
        'v' : '🅅',
        'w' : '🅆',
        'x' : '🅇',
        'y' : '🅈',
        'z' : '🅉',
        'A' : '🄰',
        'B' : '🄱',
        'C' : '🄲',
        'D' : '🄳',
        'E' : '🄴',
        'F' : '🄵',
        'G' : '🄶',
        'H' : '🄷',
        'I' : '🄸',
        'J' : '🄹',
        'K' : '🄺',
        'L' : '🄻',
        'M' : '🄼',
        'N' : '🄽',
        'O' : '🄾',
        'P' : '🄿',
        'Q' : '🅀',
        'R' : '🅁',
        'S' : '🅂',
        'T' : '🅃',
        'U' : '🅄',
        'V' : '🅅',
        'W' : '🅆',
        'X' : '🅇',
        'Y' : '🅈',
        'Z' : '🅉'
        }
        pattern = re.compile(r'(' + '|'.join(fourth_style.keys()) + r')')
        result = pattern.sub(lambda x: fourth_style[x.group()], text)
        return(result)

    def style_5(text):
        fifth_style = {
        'a' : 'ᗩ',
        'b' : 'ᗷ',
        'c' : 'ᑢ',
        'd' : 'ᕲ',
        'e' : 'ᘿ',
        'f' : 'ᖴ',
        'g' : 'ᘜ',
        'h' : 'ᕼ',
        'i' : 'ᓰ',
        'j' : 'ᒚ',
        'k' : 'ᖽᐸ',
        'l' : 'ᒪ',
        'm' : 'ᘻ',
        'n' : 'ᘉ',
        'o' : 'ᓍ',
        'p' : 'ᕵ',
        'q' : 'ᕴ',
        'r' : 'ᖇ',
        's' : 'S',
        't' : 'ᖶ',
        'u' : 'ᑘ',
        'v' : 'ᐺ',
        'w' : 'ᘺ',
        'x' : '᙭',
        'y' : 'ᖻ',
        'z' : 'ᗱ',
        'A' : 'ᗩ',
        'B' : 'ᗷ',
        'C' : 'ᑢ',
        'D' : 'ᕲ',
        'E' : 'ᘿ',
        'F' : 'ᖴ',
        'G' : 'ᘜ',
        'H' : 'ᕼ',
        'I' : 'ᓰ',
        'J' : 'ᒚ',
        'K' : 'ᖽᐸ',
        'L' : 'ᒪ',
        'M' : 'ᘻ',
        'N' : 'ᘉ',
        'O' : 'ᓍ',
        'P' : 'ᕵ',
        'Q' : 'ᕴ',
        'R' : 'ᖇ',
        'S' : 'S',
        'T' : 'ᖶ',
        'U' : 'ᑘ',
        'V' : 'ᐺ',
        'W' : 'ᘺ',
        'X' : '᙭',
        'Y' : 'ᖻ',
        'Z' : 'ᗱ'
        }
        pattern = re.compile(r'(' + '|'.join(fifth_style.keys()) + r')')
        result = pattern.sub(lambda x: fifth_style[x.group()], text)
        return(result)

def get_num_words(text):
    text_list = text.split()
    return len(text_list)

def get_letter_stats(text):
    stats = {}
    for letter in text:
        if stats.get(letter.lower()) == None:
            stats[letter.lower()] = 1
        else:
            stats[letter.lower()] += 1
    return stats

def sort_on(k): 
    return k["num"]

def create_report(results):
    report = []
    for k in results:
        if k.isalpha():
            report.append({
                "char": k,
                "num": results[k]
            }) 
    return sorted(report, reverse=True, key=sort_on)

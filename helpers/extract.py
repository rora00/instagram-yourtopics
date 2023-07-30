from bs4 import BeautifulSoup

def extract_yourtopics(fpath: str, classname: str = "_2pin _a6_q") -> list:
    """Extracts your topics from Instagram data download

    Args:
        fpath (str): Filepath of your_topics.html
        classname (str, optional): HTML class containing your topics. Defaults to "_2pin _a6_q".

    Returns:
        yourtopics (list): list containing your topics
    """
    # Check that correct file is supplied
    assert fpath[-17:] == "/your_topics.html", "File path specified does not include /your_topics.html"

    # Read the content of the file
    with open(fpath, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Create beautifulsoup object
    soup = BeautifulSoup(content, "html.parser")

    # Find all tables with class "_2pin _a6_q"
    tables = soup.find_all('td', class_=classname)

    # Create set to store your topics
    yourtopics = list()

    # Retrieve the information in the div within each table
    for table in tables:
        div_content = table.find('div').text.strip()
        yourtopics.append(div_content)

    # Check yourtopics only contain strings
    assert all([type(topic) == str for topic in yourtopics]), "Your topics contain types other than strings"

    return yourtopics
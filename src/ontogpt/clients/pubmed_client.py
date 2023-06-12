"""Pubmed Client."""
import logging
from dataclasses import dataclass
from typing import List

import inflection
import requests

PMID = str
TITLE_WEIGHT = 5
MAX_PMIDS = 50

PUBMED = "pubmed"
EUTILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


def _normalize(s: str) -> str:
    return inflection.singularize(s).lower()


# TODO: Add this back
# def _score_paper(paper: PubmedArticle, keywords: List[str]) -> int:
#     title_score = _score_text(paper.title, keywords)
#     abstract_score = _score_text(paper.abstract, keywords)
#     logging.info(f"Scored {paper.pmid} {paper.title} with TS={title_score} AS={abstract_score} ")
#     return title_score * TITLE_WEIGHT + abstract_score


# def _score_text(text: str, keywords: List[str]) -> int:
#     text = text.lower()
#     if not text:
#         return -100
#     score = 0
#     for kw in keywords:
#         if kw in text:
#             score += 1
#     return score


@dataclass
class PubmedClient:
    """A client for the Pubmed API.

    This class is a wrapper around the Entrez API.
    """

    max_text_length = 3000

    # TODO: allow passing email since NCBI wants to know

    def get_pmids(self, term: str) -> List[str]:
        """Search PubMed and retrieve a list of PMIDs matching the search term.

        :param term: The search term to query PubMed.
        :return: A list of PMIDs matching the search term.
        """

        pmids = []

        batch_size = 250

        search_url = EUTILS_URL + "esearch.fcgi"

        # If retmax==0, we get only the size of the search result in count of PMIDs
        params = {"db": PUBMED, "term": term, "retmode": "json", "retmax": 0}
        response = requests.get(search_url, params=params)

        if response.status_code == 200:
            data = response.json()
            resultcount = int(data["esearchresult"]["count"])
            logging.info(f"Search returned {resultcount} PMIDs matching search term {term}")
        else:
            print("Encountered error in searching PubMed:", response.status_code)

        # Now we get the list of PMIDs, iterating as needed

        # TODO: handle error 429 - otherwise results get truncated early

        for retstart in range(0, resultcount, batch_size):
            params['retstart'] = retstart
            params['retmax'] = batch_size

            response = requests.get(search_url, params=params)

            if response.status_code == 200:
                data = response.json()
                pmids.extend(data['esearchresult']['idlist'])
            else:
                print("Encountered error in searching PubMed:", response.status_code)

        return pmids

    # TODO: parse xml output with beautifulsoup
    # TODO: verify the text() function works as expected for both single and multiple entries

    def text(self, id: list[PMID], autoformat=True) -> str:
        """Get the text of one or more papers from their PMIDs.

        :param ids: List of PubMed IDs
        :param autoformat: if True include title and abstract concatenated
        :return: the text of a single entry, or concatenated text of multiple entries
        """

        fetch_url = EUTILS_URL + "efetch.fcgi"
        params = {
            'db': PUBMED,
            'id': ','.join(id),
            'rettype': 'xml', 
            'retmode': 'xml'
        }

        response = requests.get(fetch_url, params=params)

        if response.status_code == 200:
            xml_data = response.text
            print(xml_data)
        else:
            print("Encountered error in fetching from PubMed:", response.status_code)

        # TODO: concatenate as needed
        if len(id) == 1:
            txt = xml_data
        else:
            txt = xml_data

        # for pa in paset:
        #     if autoformat:
        #         txt = f"Title: {pa.title}\nAbstract: {pa.abstract}\nKeywords: {'; '.join(pa.mesh_headings)}"  # noqa
        #     else:
        #         txt = pa.full_text
        # if len(txt) > self.max_text_length:
        #     logging.warning(f"Truncating text: {txt[:self.max_text_length]}...")
        #     txt = txt[0 : self.max_text_length]
        return txt

    # def search(self, term: str, keywords: List[str] = None) -> Iterator[PMID]:
    #     """Get the text of a paper from its PMID.

    #     :param term:
    #     :param keywords:
    #     :return:
    #     """
    #     print("Getting client")
    #     ec = self.entrez_client
    #     if keywords:
    #         keywords = [_normalize(kw) for kw in keywords]
    #         term = f"({term}) AND ({' OR '.join(keywords)})"
    #     logging.info(f"Searching for {term}...")
    #     esr = ec.esearch(db="pubmed", term=term)
    #     logging.info(f"Found {esr.count} papers for {term}.")
    #     paset = ec.efetch(db="pubmed", id=esr.ids[0:MAX_PMIDS])
    #     keywords = keywords or []
    #     keywords = [_normalize(kw) for kw in keywords]
    #     scored_papers = [(_score_paper(paper, keywords), paper) for paper in paset]
    #     scored_papers.sort(key=lambda x: x[0], reverse=True)
    #     for score, paper in scored_papers:
    #         logging.debug(f"Yielding {paper.pmid} {paper.title} with score {score} ")
    #         yield f"PMID:{paper.pmid}"

import requests

from bs4 import BeautifulSoup


def Points_table():
    # Printing the points like table wise :

    print("\n", "=" * 20, iplhead[0].text, "=" * 20)
    print('\n', team[0].text, " " * 20, match[0].text, " ", match_won[0].text, " ",
          match_lost[0].text, " ", match_tied[0].text, " ", match_NR[0].text, " ",
          match_points[0].text, " ", match_NRR[0].text)
    print("\n")
    print(team_all[0].text)

    print("\t" * 7, MI_pts[0].text, " " * 3, MI_pts[1].text, " " * 3, MI_pts[2].text,
          " " * 3, MI_pts[3].text, " " * 3, MI_pts[4].text, " " * 3, MI_pts[5].text, " " * 3, MI_pts[6].text, "\n")

    print(team_all[1].text)

    print("\t" * 7, MI_pts[7].text, " " * 3, MI_pts[8].text, " " * 3, MI_pts[9].text,
          " " * 3, MI_pts[10].text, " " * 3, MI_pts[11].text, " " * 3, MI_pts[12].text, " " * 3, MI_pts[13].text, "\n")

    print(team_all[2].text)

    print("\t" * 7, MI_pts[14].text, " " * 3, MI_pts[15].text, " " * 3, MI_pts[16].text,
          " " * 3, MI_pts[17].text, " " * 3, MI_pts[18].text, " " * 3, MI_pts[19].text, " " * 3, MI_pts[20].text, "\n")

    print(team_all[3].text)

    print("\t" * 7, MI_pts[21].text, " " * 3, MI_pts[22].text, " " * 3, MI_pts[23].text,
          " " * 3, MI_pts[24].text, " " * 3, MI_pts[25].text, " " * 3, MI_pts[26].text, " " * 3, MI_pts[27].text, "\n")

    print(team_all[4].text)

    print("\t" * 7, MI_pts[28].text, " " * 3, MI_pts[29].text, " " * 3, MI_pts[30].text,
          " " * 3, MI_pts[31].text, " " * 3, MI_pts[32].text, " " * 3, MI_pts[33].text, " " * 3, MI_pts[34].text, "\n")

    print(team_all[5].text)

    print("\t" * 7, MI_pts[35].text, " " * 3, MI_pts[36].text, " " * 3, MI_pts[37].text,
          " " * 3, MI_pts[38].text, " " * 3, MI_pts[39].text, " " * 3, MI_pts[40].text, " " * 3, MI_pts[41].text, "\n")

    print(team_all[6].text)

    print("\t" * 7, MI_pts[42].text, " " * 3, MI_pts[43].text, " " * 3, MI_pts[44].text,
          " " * 3, MI_pts[45].text, " " * 3, MI_pts[46].text, " " * 3, MI_pts[47].text, " " * 3, MI_pts[48].text, "\n")

    print(team_all[7].text)

    print("\t" * 7, MI_pts[49].text, " " * 3, MI_pts[50].text, " " * 3, MI_pts[51].text,
          " " * 3, MI_pts[52].text, " " * 3, MI_pts[53].text, " " * 3, MI_pts[54].text, " " * 3, MI_pts[55].text, "\n")


if __name__ == '__main__':
    # ===============copy link address
    link = "https://www.cricbuzz.com/cricket-series/3130/indian-premier-league-2020/points-table"

    req = requests.get(link)  # =  get request from websites

    soup = BeautifulSoup(req.text, 'html.parser')  # Given beauty Like html Text

    # ====All websites Main data following:

    iplhead = soup.find_all('h3', class_='cb-mat-mnu-wrp cb-min-pad')

    team = soup.find_all('th', class_="cb-srs-pnts-th text-left")

    match = soup.find_all('td', title="Matches Played")

    match_won = soup.find_all('td', title="Matches Won")

    match_lost = soup.find_all('td', title="Matches Lost")

    match_tied = soup.find_all('td', title="Matches Tied")

    match_NR = soup.find_all('td', title="Matches with No Result")

    match_points = soup.find_all('th', title="Match Points")

    match_NRR = soup.find_all('td', title="Net Run Rate")

    team_all = soup.find_all('td', class_='cb-srs-pnts-name')

    MI_pts = soup.find_all('td', class_="cb-srs-pnts-td")

    # Calling function :

    Points_table()

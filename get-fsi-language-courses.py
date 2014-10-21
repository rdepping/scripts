#!/usr/bin/env python3.4

# http://pyright.blogspot.ie/2014/10/downloading-bunch-of-mp3s-off-internet.html

from urllib import request
from urllib.parse import quote

# For getting foreign language study mp3's.
# Main part of URL for French.
BASEURL = 'http://www.fsi-language-courses.org/Courses/'
MIDDLEURLI = 'French/Basic (Revised)/Volume {volume}/'
MIDDLEURLII = 'French/Basic (Revised)/Volume {0:s}/'
BASEURLEND = 'FSI - French Basic Course (Revised) '

# Format changes inexplicably at chapter 19.
# Grrrr . . .
URLI = BASEURL + MIDDLEURLI + BASEURLEND
URLI += '- Volume {volume} - Unit {unit:0>2d} '
URLI += '{unit:0>2d}.{section:0>2d}.mp3'

URLII = BASEURL + MIDDLEURLII + BASEURLEND
URLII += '- Volume {1[volume]:d} - Unit {1[unit]:0>2d} '
URLII += '{1[unit]:0>2d}.{1[section]:d}.mp3'

# Format for actual name of mp3 files.
# This is what I wanted for a name - your
# preferences may be different - adjust
# accordingly.
FILENAME = '{unit:0>2d}{section:0>2d}.mp3'

# Texts (pdf format).
# Everything the State Dept. does is a 'StudentText' -
# fair enough.
STUDENTTXT = 'StudentText.pdf'

PDFURLBASICTEXT1 = 'http://ia601400.us.archive.org/28/items/'
PDFURLBASICTEXT1 += 'Fsi-FrenchBasicCourserevised-StudentText/'
PDFURLBASICTEXT1 += 'Fsi-FrenchBasicCourserevised-Volume1-'

PDFURLBASICTEXT2 = 'http://ia801400.us.archive.org/28/items/'
PDFURLBASICTEXT2 += 'Fsi-FrenchBasicCourserevised-StudentText/'
PDFURLBASICTEXT2 += 'Fsi-FrenchBasicCourserevised-Volume2-'

PDFURLMONDEFR = 'http://ia600406.us.archive.org/3/items/'
PDFURLMONDEFR += 'Fsi-LeMondeFrancophone/Fsi-LeMondeFrancophone-'

TWO = 'Two'

# Tack on StudentText.pdf to end.
pdfs = [PDFURLBASICTEXT1, PDFURLBASICTEXT2, PDFURLMONDEFR]
pdfs = [pdfx + STUDENTTXT for pdfx in pdfs]
myfilenames = ['basictext1.pdf', 'basictext2.pdf', 'mondefrancophone.pdf']
# I'm using the dictionary keys for filenames.
pdfs = dict(zip(myfilenames, pdfs))

VOLUME = 'volume'
UNIT = 'unit'
SECTION = 'section'

# volume key, then list of two tuples of unit and 
# number of sections
VOLUMES = {1:[(1, 6), (2, 6), (3, 6), (4, 7), (5, 7), 
              (6, 3), (7, 11), (8, 10), (9, 11), (10, 9),
              (11, 9), (12, 4)],
           2:[(13, 8), (14, 9), (15, 10), (16, 9), (17, 11),
              (18, 7), (19, 9), (20, 8), (21, 8), (22, 7),
              (23, 8), (24, 6)]}

mp3s = []
for key in VOLUMES:
    for unitsection in VOLUMES[key]:
        for x in range(1, unitsection[1] + 1):
            mp3s.append({VOLUME:key, UNIT:unitsection[0], SECTION:x})

for mp3x in mp3s:
    # Name format change at chapter 19 :-(
    if mp3x[UNIT] > 18:
        urlx = URLII.format(TWO, mp3x)
    else:
        urlx = URLI.format(**mp3x)
    filenamex = FILENAME.format(**mp3x)
    print('Retrieving {0} . . .'.format(urlx))
    request.urlretrieve(quote(urlx, safe="/:"), filenamex)

# Add pdf texts at end.
for pdfx in pdfs:
    print('Retrieving {0} . . .'.format(pdfx))
    request.urlretrieve(quote(pdfs[pdfx], safe="/:"), pdfx)

print('Everything appears to have downloaded.')
print('Check the directory with the files to be sure.')

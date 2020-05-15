import tab_files as tf
import os
import numpy as np
import guitarpro
import msgpack

batch_count = 2
maxBeats = 8
batch_length = 30200

def duration(val):
    l = [2 ** i for i in range(7)]
    min = 1000
    out = 0
    for i in l:
        if abs(val - i) < min:
            min = abs(val - i)
            out = i
    return out


def enters(val):
    l = [i + 1 for i in range(13)]
    min = 1000
    out = 0
    for i in l:
        if abs(val - i) < min:
            min = abs(val - i)
            out = i
    return out


def returnTestData(g):
    x = np.zeros((len(g.measures), maxBeats, 7), dtype=float)
    i = -1
    for gm in g.measures:
        i += 1
        if len(gm.beats) <= maxBeats:
            j = 0
            for gb in gm.beats:
                if len(gb.notes) > 0:
                    x[i][j][0] = 1
                    x[i][j][1] = len(gb.notes)
                x[i][j][2] = 1 / gb.duration
                j += 1

    return x


def makeTab(guitarTracks, y, names, path):
    print('start saving')
    notes = [38, 92, 35, 47, 1, 99]
    # 'FICHIER GUITAR PRO v5.00'
    tab = guitarpro.models.Song()
    tab.tempo = guitarTracks[0].song.tempo
    tab.version = 'FICHIER GUITAR PRO v3.00'
    tab.tracks = guitarTracks

    for predict, name in zip(y, names):
        predict = predict.tolist()
        tab.tracks.append(guitarpro.Track(tab))
        num = len(tab.tracks) - 1

        tab.tracks[num].number = 1
        tab.tracks[num].name = name
        tab.tracks[num].isPercussionTrack = True

        tab.tracks[num].channel.volume = 120
        tab.tracks[num].channel.balance = 64

        for s in tab.tracks[num].strings:
            s.value = 0
        tab.tracks[num].measures = []
        m = -1
        for measure in predict:
            measureHeader = guitarpro.models.MeasureHeader()
            tab.tracks[num].measures.append(guitarpro.Measure(tab.tracks[num], measureHeader))
            m += 1
            if m > len(guitarTracks[0].measures) - 1:
                break
            tab.tracks[num].measures[m].timeSignature.numerator = guitarTracks[0].measures[m].timeSignature.numerator
            tab.tracks[num].measures[m].timeSignature.denominator.value = guitarTracks[0].measures[
                m].timeSignature.denominator.value
            tab.tracks[num].measures[m].voices = [guitarpro.Voice(tab.tracks[num].measures[m])]
            b = -1
            for beat in measure:
                tab.tracks[num].measures[m].voices[0].beats.append(guitarpro.Beat(tab.tracks[num].measures[m].voices[0]))
                b += 1

                tab.tracks[num].measures[m].voices[0].beats[b].status = guitarpro.BeatStatus.rest
                j = 0
                string = 1
                while j < 5:
                    if beat[1 + j] > 0.5:
                        tab.tracks[num].measures[m].voices[0].beats[b].status = guitarpro.BeatStatus.normal
                        tab.tracks[num].measures[m].voices[0].beats[b].notes.append(
                            guitarpro.Note(tab.tracks[num].measures[m].voices[0].beats[b]))
                        tab.tracks[num].measures[m].voices[0].beats[b].notes[string - 1].value = notes[j]
                        tab.tracks[num].measures[m].voices[0].beats[b].notes[string - 1].string = string
                        tab.tracks[num].measures[m].voices[0].beats[b].notes[string - 1].velocity = 127
                        tab.tracks[num].measures[m].voices[0].beats[b].notes[
                            string - 1].type = guitarpro.NoteType.normal
                        string += 1
                    j += 1

                tab.tracks[num].measures[m].voices[0].beats[b].duration.value = duration(1 / beat[0])
                tab.tracks[num].measures[m].voices[0].beats[b].duration.isDotted = False
                tab.tracks[num].measures[m].voices[0].beats[b].duration.isDoubleDotted = False
                tab.tracks[num].measures[m].voices[0].beats[b].duration.tuplet.enters = 1
                tab.tracks[num].measures[m].voices[0].beats[b].duration.tuplet.times = 1

    # tab.tracks = [tab.tracks[1]]
    guitarpro.write(tab, path)


def addTrack(base_track, y, name, tab):
    print('start saving')
    notes = [38, 92, 35, 47, 93, 99]
    #tab.tempo = guitarTracks[0].song.tempo
    #tab.version = 'FICHIER GUITAR PRO v3.00'
    #tab.tracks = guitarTracks

    y = y.tolist()
    tab.tracks.append(guitarpro.Track(tab))
    num = len(tab.tracks) - 1

    tab.tracks[num].number = 1
    tab.tracks[num].name = name
    tab.tracks[num].isPercussionTrack = True
    for s in tab.tracks[num].strings:
        s.value = 0
    tab.tracks[num].measures = []
    m = -1
    for measure in y:
        measureHeader = guitarpro.models.MeasureHeader()
        tab.tracks[num].measures.append(guitarpro.Measure(tab.tracks[num], measureHeader))
        m += 1
        if m > len(base_track.measures) - 1:
            break
        tab.tracks[num].measures[m].timeSignature.numerator = base_track.measures[m].timeSignature.numerator
        tab.tracks[num].measures[m].timeSignature.denominator.value = base_track.measures[
            m].timeSignature.denominator.value
        tab.tracks[num].measures[m].voices = [guitarpro.Voice(tab.tracks[num].measures[m])]
        b = -1
        takt = tab.tracks[num].measures[m].timeSignature.numerator / tab.tracks[num].measures[m].timeSignature.denominator.value
        takti = 0
        for beat in measure:
            if beat[0] >= 0.03125 and takti + 1 / duration(1 / beat[0]) <= takt:
                takti += 1 / duration(1 / beat[0])
                tab.tracks[num].measures[m].voices[0].beats.append(
                    guitarpro.Beat(tab.tracks[num].measures[m].voices[0]))
                b += 1

                tab.tracks[num].measures[m].voices[0].beats[b].status = guitarpro.BeatStatus.rest
                j = 0
                string = 1
                while j < 5:
                    if beat[1 + j] > 0.5:
                        tab.tracks[num].measures[m].voices[0].beats[b].status = guitarpro.BeatStatus.normal
                        tab.tracks[num].measures[m].voices[0].beats[b].notes.append(
                            guitarpro.Note(tab.tracks[num].measures[m].voices[0].beats[b]))
                        tab.tracks[num].measures[m].voices[0].beats[b].notes[string - 1].value = notes[j]
                        tab.tracks[num].measures[m].voices[0].beats[b].notes[string - 1].string = string
                        tab.tracks[num].measures[m].voices[0].beats[b].notes[string - 1].velocity = 127
                        tab.tracks[num].measures[m].voices[0].beats[b].notes[
                            string - 1].type = guitarpro.NoteType.normal
                        string += 1
                    j += 1

                tab.tracks[num].measures[m].voices[0].beats[b].duration.value = duration(1 / beat[0])
                tab.tracks[num].measures[m].voices[0].beats[b].duration.isDotted = False
                tab.tracks[num].measures[m].voices[0].beats[b].duration.isDoubleDotted = False
                tab.tracks[num].measures[m].voices[0].beats[b].duration.tuplet.enters = 1
                tab.tracks[num].measures[m].voices[0].beats[b].duration.tuplet.times = 1

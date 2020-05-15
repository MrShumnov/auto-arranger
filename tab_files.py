import guitarpro
from abc import ABCMeta, abstractmethod


class Track:
    __metaclass__ = ABCMeta

    @abstractmethod
    def Scan(self):
        """заполняет все массивы"""


class Note:
    def __init__(self, value):
        self.value = value


class Beat:
    def __init__(self, duration, isDotted, isDoubleDotted, enters, times):
        self.notes = []

        self.duration = duration
        self.isDotted = isDotted
        self.isDoubleDotted = isDoubleDotted
        self.enters = enters
        self.times = times


class Measure:
    def __init__(self, upNum, downNum):
        self.upNum = upNum
        self.downNum = downNum
        self.beats = []
        self.empty = True
        self.dotted = False
        self.doubledotted = False


class GuitarTrack(Track):
    def __init__(self, track):
        self.strings = []
        self.measures = []
        self.name = track.name
        self.first_string = track.strings[len(track.strings) - 1].value

        last = track.strings[len(track.strings) - 1].value
        for i in track.strings:
            self.strings.append(i.value - last)
        self.Scan(track)

    def Scan(self, track):
        i = -1
        for measure in track.measures:
            self.measures.append(Measure(measure.timeSignature.numerator, measure.timeSignature.denominator.value))
            i += 1
            j = -1
            for beat in measure.voices[0].beats:
                self.measures[i].beats.append(Beat(beat.duration.value, beat.duration.isDotted, beat.duration.isDoubleDotted,
                                       beat.duration.tuplet.enters, beat.duration.tuplet.times))
                if beat.duration.isDotted:
                    self.measures[i].dotted = True
                if beat.duration.isDoubleDotted:
                    self.measures[i].doubledotted = True
                j += 1
                for note in beat.notes:
                    threat = note.value
                    string = note.string
                    val = threat + self.strings[string - 1] + track.strings[len(track.strings) - 1].value
                    self.measures[i].beats[j].notes.append(Note(val))
                    self.measures[i].empty = False


class DrumsTrack(Track):
    def __init__(self, track):
        self.measures = []
        self.Scan(track)

    def Scan(self, track):
        i = -1
        for measure in track.measures:
            self.measures.append(Measure(measure.timeSignature.numerator, measure.timeSignature.denominator.value))
            i += 1
            j = -1
            for beat in measure.voices[0].beats:
                self.measures[i].beats.append(Beat(beat.duration.value, beat.duration.isDotted, beat.duration.isDoubleDotted,
                                       beat.duration.tuplet.enters, beat.duration.tuplet.times))
                if beat.duration.isDotted:
                    self.measures[i].dotted = True
                if beat.duration.isDoubleDotted:
                    self.measures[i].doubledotted = True

                j += 1
                for note in beat.notes:
                    self.measures[i].beats[j].notes.append(Note(note.value))
                    self.measures[i].empty = False


class Tab:

    def __init__(self, s):
        self.guitarTracks = []
        self.drumsTrack = []
        self.bassTrack = []
        tab = guitarpro.parse(s)
        self.tempo = tab.tempo
        self.version = tab.version

        for i in tab.tracks:
            if not i.isPercussionTrack:
                if len(i.strings) >= 6:
                    self.guitarTracks.append(GuitarTrack(i))
                else:
                    if len(i.strings) == 4:
                        self.bassTrack.append(GuitarTrack(i))
            else:
                self.drumsTrack.append(DrumsTrack(i))

    def SaveTab(self, g, d, name):

        t = guitarpro.models.Song()
        t.tempo = self.tempo
        t.version = self.version
        t.tracks = []

        self.AddGuitarTrack(self.guitarTracks[g], t)
        self.AddDrumsTrack(self.drumsTrack[d], t)

        guitarpro.write(t, name)

    def AddGuitarTrack(self, track, t):
        t.tracks.append(guitarpro.Track(t))
        tn = len(t.tracks) - 1

        t.tracks[tn].measures = []
        m = -1
        for measure in track.measures:
            measureHeader = guitarpro.models.MeasureHeader()
            t.tracks[tn].measures.append(guitarpro.Measure(t.tracks[tn], measureHeader))
            m += 1
            t.tracks[tn].measures[m].timeSignature.numerator = measure.upNum
            t.tracks[tn].measures[m].timeSignature.denominator.value = measure.downNum
            t.tracks[tn].measures[m].voices = [guitarpro.Voice(t.tracks[tn].measures[m])]
            b = -1
            for beat in measure.beats:
                t.tracks[tn].measures[m].voices[0].beats.append(guitarpro.Beat(t.tracks[tn].measures[m].voices[0]))
                b += 1

                if len(beat.notes) > 0:
                    val = beat.notes[len(beat.notes) - 1].value
                    t.tracks[tn].measures[m].voices[0].beats[b].notes.append(
                        guitarpro.Note(t.tracks[tn].measures[m].voices[0].beats[b]))
                    string = 5
                    for k in track.strings:
                        if val > 25:
                            string -= 1
                            val = beat.notes[len(beat.notes) - 1].value - track.strings[string]
                    t.tracks[tn].measures[m].voices[0].beats[b].notes[0].value = val
                    t.tracks[tn].measures[m].voices[0].beats[b].notes[0].string = string + 1
                    t.tracks[tn].measures[m].voices[0].beats[b].notes[0].velocity = 127
                    t.tracks[tn].measures[m].voices[0].beats[b].notes[0].type = guitarpro.NoteType.normal
                    t.tracks[tn].measures[m].voices[0].beats[b].status = guitarpro.BeatStatus.normal
                else:
                    t.tracks[tn].measures[m].voices[0].beats[b].status = guitarpro.BeatStatus.rest

                t.tracks[tn].measures[m].voices[0].beats[b].duration.value = beat.duration
                t.tracks[tn].measures[m].voices[0].beats[b].duration.isDotted = beat.isDotted
                t.tracks[tn].measures[m].voices[0].beats[b].duration.isDoubleDotted = beat.isDoubleDotted
                t.tracks[tn].measures[m].voices[0].beats[b].duration.tuplet.enters = beat.enters
                t.tracks[tn].measures[m].voices[0].beats[b].duration.tuplet.times = beat.times

    def AddDrumsTrack(self, track, t):
        t.tracks.append(guitarpro.Track(t))
        tn = len(t.tracks) - 1

        t.tracks[tn].isPercussionTrack = True
        for s in t.tracks[tn].strings:
            s.value = 0
        t.tracks[tn].measures = []
        m = -1
        for measure in track.measures:
            measureHeader = guitarpro.models.MeasureHeader()
            t.tracks[tn].measures.append(guitarpro.Measure(t.tracks[tn], measureHeader))
            m += 1
            t.tracks[tn].measures[m].timeSignature.numerator = measure.upNum
            t.tracks[tn].measures[m].timeSignature.denominator.value = measure.downNum
            t.tracks[tn].measures[m].voices = [guitarpro.Voice(t.tracks[tn].measures[m])]
            b = -1
            for beat in measure.beats:
                t.tracks[tn].measures[m].voices[0].beats.append(guitarpro.Beat(t.tracks[tn].measures[m].voices[0]))
                b += 1

                if len(beat.notes) > 0:
                    string = 1
                    n = -1
                    for note in beat.notes:
                        t.tracks[tn].measures[m].voices[0].beats[b].notes.append(
                            guitarpro.Note(t.tracks[tn].measures[m].voices[0].beats[b]))
                        n += 1
                        t.tracks[tn].measures[m].voices[0].beats[b].notes[n].value = note.value
                        t.tracks[tn].measures[m].voices[0].beats[b].notes[n].string = string
                        string += 1
                        t.tracks[tn].measures[m].voices[0].beats[b].notes[n].velocity = 127
                        t.tracks[tn].measures[m].voices[0].beats[b].notes[n].type = guitarpro.NoteType.normal
                    t.tracks[tn].measures[m].voices[0].beats[b].status = guitarpro.BeatStatus.normal
                else:
                    t.tracks[tn].measures[m].voices[0].beats[b].status = guitarpro.BeatStatus.rest

                t.tracks[tn].measures[m].voices[0].beats[b].duration.value = beat.duration
                t.tracks[tn].measures[m].voices[0].beats[b].duration.isDotted = beat.isDotted
                t.tracks[tn].measures[m].voices[0].beats[b].duration.isDoubleDotted = beat.isDoubleDotted
                t.tracks[tn].measures[m].voices[0].beats[b].duration.tuplet.enters = beat.enters
                t.tracks[tn].measures[m].voices[0].beats[b].duration.tuplet.times = beat.times

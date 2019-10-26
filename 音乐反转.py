from pydub import AudioSegment
from pydub.playback import play


t = AudioSegment.from_file("C:/Users/admin/AppData/Local/Programs/Python/Python37/Hao/123.mp3", 'mp3')
b = t.reverse()
b.export("倒放.mp3", format="mp3")
play(t)
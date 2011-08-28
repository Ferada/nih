from os.path import join, exists, abspath
from os import mkdir
from models import QueueItem, ChatItem
from metadata import get_metadata
from Queue import Queue
from django.conf import settings

cacheFolder = settings.CACHE_FOLDER

def is_cached(item):
	hash = item.hash()
	cacheFile = join(cacheFolder, hash)
	return exists(cacheFile)

def cached(item):
	hash = item.hash()
	cacheFile = join(cacheFolder, hash)
	if not is_cached(item):
		from downloader import downloader
		downloader.add(item)
		return None
	
	if not item.got_metadata:
		metadata = get_metadata(cacheFile)
		item.artist = metadata.get("artistName", "")
		item.album = metadata.get("albumTitle", "")
		item.title = metadata.get("trackName", "")
		item.trackLength = metadata.get("totalTime", 0)
		item.trackNumber = metadata.get("trackNumber", "0")
		item.got_metadata = True
		item.save()

	return abspath(cacheFile)

def albumArt(item):
	cacheFile = join(cacheFolder, item.hash() + ".jpeg")
	if exists(cacheFile):
		return cacheFile
	else:
		return None

if not exists(cacheFolder):
	mkdir(cacheFolder)
for x in QueueItem.objects.all():
	cached(x.what)

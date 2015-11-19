# nih

Not Invented Here (a jukebox)

## Deploy

* `git clone https://github.com/lshift/nih.git`
* `./scripts/bootstrap.sh` (which will use `sudo` internally to get root)
* `sudo python scripts/deploy.py`

This will create `/usr/share/nih`, and an Apache site pointing at the most recently deployed version. Default port is 8888, for historical reasons.

See [Versioned Deployment](docs/VersionedDeployment.md) for more on how deployment is handled.

By default, the deploy script will wait until the Jukebox is idle (not playing any music) before making any changes, so you can deploy away without any worry of an interruption to the music. Use `--help` to learn how to change the default settings.

### Deploy an update

To deploy new versions:
* `git pull`
* `sudo python scripts/deploy.py`

Each time you run deploy a new timestamped directory will be created in `/usr/share/nih`. A symlink `/usr/share/nih/current` always points to the most recent deploy, and `/usr/share/nih/previous` points to the version before (if any).

### Rollback a deploy

To rollback just `rm -r /usr/share/nih/current`, and rename `previous` to `current`. 

This will rollback the application, as well as the Apache site configuration, but it will not rollback the database. You can do this separately by running

`mysql jukebox < /usr/share/nih/previous/db-backup.sql`

Note that if you have already renamed `previous` to `current` then `db-backup.sql` will now be in `current`.

## Develop
* `git clone git@github.com:lshift/nih.git`
* `sudo sh scripts/bootstrap.sh`

Bootstrap will
* Install dependencies using apt-get and pip (the apt-get stage installs pip, if you don't already have it)
* Create a database and apply migrations to it (you can edit `src/db_settings.py` to change the database credentials)
* Checkout dependencies that are not available as packages using `git submodule`

You can then develop using the Django development server, or deploy to Apache as above

## Scrobbling
This is disabled by default. You can enable it by changing `settings.LASTFM_ENABLED` to true. There are credentials for a Last.fm 'test_erlang' account in the settings file.

from geoloc.datamodels.location_info import CityStateLocationInfo
from geoloc.logger.log_utils import LogUtils
from geoloc.services.geoloc_services import get_geoloc_from_state_and_city, get_geoloc_from_zip_code
import click

log_utils = LogUtils(file_name="logs/geoloc-util.log")
logger = log_utils.get_logger()


def get_geo_loc(all_locations: str | list[str]) -> list:
    rc_message = []
    for location in all_locations:
        logger.debug(f"Input data: {location}")
        logger.debug(f"Check if the input has ','to identify state, city or zip")
        if "," in location:
            logger.info("City, State value is given")
            city_state = location.split(",")
            rc_message.append(get_geoloc_from_state_and_city(city=city_state[0].strip(), state=city_state[1].strip()))
        else:
            rc_message.append(get_geoloc_from_zip_code(zip_code=location.strip()))
    return rc_message


@click.command()
@click.option('--locations', multiple=True,
              help='Send either a zip code or city, state name, single or multiple values')
@click.argument('additional_locations', nargs=-1)
def cli(locations: str, additional_locations: str):
    all_locations = list(locations) + list(additional_locations)
    rc_values = get_geo_loc(all_locations)
    for count, rc in enumerate(rc_values):
        if "error" in rc:
            click.echo(all_locations[count] + ":" + rc["error"])
            click.echo("-" * 40)
        else:
            if isinstance(rc, CityStateLocationInfo):
                click.echo(f"City: {rc.name}\n"
                           f"Country: {rc.country}\n"
                           f"State: {rc.state}\n"
                           f"Latitude: {rc.lat}\n"
                           f"Longitude: {rc.lon}")
            else:
                click.echo(f"Zip: {rc.zip}\n"
                           f"Country: {rc.country}\n"
                           f"State: {rc.name}\n"
                           f"Latitude: {rc.lat}\n"
                           f"Longitude: {rc.lon}")
            click.echo("-" * 40)
import time
import threading

from event import (
    Event,
    Template)
from mouse import Mouse
from output import output_message
from screen import Screen


mouse = Mouse()
screen = Screen()


def run():
    accept_match()


def in_lobby_event_callback(location):
    output_message('MATCH FOUND: press any key to restart the EZ Queue')
    input()
    accept_match()


def accept_match_event_callback(location):
    output_message('ACCEPTING MATCH')
    mouse.move((location[0] + 80, location[1] + 24))
    time.sleep(0.2)
    mouse.click()

    output_message('MATCH ACCEPTED, EZ')
    in_lobby_template = Template('edit-masteries.jpg', 0.53)
    in_lobby_event = Event(
        in_lobby_template, in_lobby_event_callback,
        12, accept_match)
    screen.assign_event(in_lobby_event)


def accept_match():
    output_message('start the queue, EZ Queue got you covered 8)')
    accept_match_template = Template('accept-match.jpg', 0.5)
    accept_match_event = Event(
        accept_match_template, accept_match_event_callback)
    screen.assign_event(accept_match_event)


if __name__ == '__main__':
    run()

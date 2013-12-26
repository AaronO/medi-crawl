# Imports
import sys
import json
import os
from os import path

def slide_url(part_url, slide_id):
    return "http://sjt.webaula.com.br/Cursos/%s/Slide%d.jpg" % (part_url, slide_id)

def url_part(course, topic_count, part_id):
    return "%s/modulo1/topico%d/%s" % (course, topic_count, part_id)

def folder_part(course, topic_count, part_id):
    return path.join(
        path.dirname(__file__),
        "data",
        course,
        "topico%d" % topic_count,
        part_id
    )

def rtmpdump_cmd(course, url_topic, dest):
    return "rtmpdump -r rtmp://fmsev.webaula.com.br:1935/sjt/%s -y %s -o %s" % (course, url_topic, dest)

def parse_course(course):
    course_id = course['id']
    title = course['title']
    topics = course['topics']

    topics_cmds = sum([
        parse_topic(course_id, t, i)
        for t, i in zip(topics, range(1, len(topics)+1))
    ], [])

    return os.linesep.join(topics_cmds)

def parse_topic(course_id, topic_data, topic_id):
    return sum([
        parse_topic_part(course_id, topic_id, part)
        for part in topic_data
    ], [])

def parse_topic_part(course_id, topic_id, data):
    part_id = data['id']
    img_count = data['img']

    part_url = url_part(course_id, topic_id, part_id)
    part_folder = folder_part(course_id, topic_id, part_id)

    img_urls = [
        slide_url(part_url, i)
        for i in range(1, img_count+1)
    ]

    wget_commands = [
        "curl %s > %s" % (
            url,
            path.join(
                part_folder,
                path.basename(url)
            )
        )
        for url in img_urls
    ]

    return sum([
        # make the folder
        ['mkdir -p %s' % part_folder],

        # Download the images
        wget_commands,

        # Download the video
        [rtmpdump_cmd(course_id, part_url, path.join(part_folder, 'video.flv'))]
    ], [])

def main():
    if len(sys.argv) < 2:
        return

    # Parse file
    return parse_course(json.load(open(sys.argv[1])))

if __name__ == '__main__':
    print main()

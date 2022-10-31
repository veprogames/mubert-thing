import argparse
import pat
import generate
import random

TAG_STRING = "tribal,action,kids,neo-classic,run 130,pumped,jazz / funk,ethnic,dubtechno,reggae,acid jazz,liquidfunk,funk,witch house,tech house,underground,artists,mystical,disco,sensorium,r&b,agender,psychedelic trance / psytrance,peaceful,run 140,piano,run 160,setting,meditation,christmas,ambient,horror,cinematic,electro house,idm,bass,minimal,underscore,drums,glitchy,beautiful,technology,tribal house,country pop,jazz & funk,documentary,space,classical,valentines,chillstep,experimental,trap,new jack swing,drama,post-rock,tense,corporate,neutral,happy,analog,funky,spiritual,sberzvuk special,chill hop,dramatic,catchy,holidays,fitness 90,optimistic,orchestra,acid techno,energizing,romantic,minimal house,breaks,hyper pop,warm up,dreamy,dark,urban,microfunk,dub,nu disco,vogue,keys,hardcore,aggressive,indie,electro funk,beauty,relaxing,trance,pop,hiphop,soft,acoustic,chillrave / ethno-house,deep techno,angry,dance,fun,dubstep,tropical,latin pop,heroic,world music,inspirational,uplifting,atmosphere,art,epic,advertising,chillout,scary,spooky,slow ballad,saxophone,summer,erotic,jazzy,energy 100,kara mar,xmas,atmospheric,indie pop,hip-hop,yoga,reggaeton,lounge,travel,running,folk,chillrave & ethno-house,detective,darkambient,chill,fantasy,minimal techno,special,night,tropical house,downtempo,lullaby,meditative,upbeat,glitch hop,fitness,neurofunk,sexual,indie rock,future pop,jazz,cyberpunk,melancholic,happy hardcore,family / kids,synths,electric guitar,comedy,psychedelic trance & psytrance,edm,psychedelic rock,calm,zen,bells,podcast,melodic house,ethnic percussion,nature,heavy,bassline,indie dance,techno,drumnbass,synth pop,vaporwave,sad,8-bit,chillgressive,deep,orchestral,futuristic,hardtechno,nostalgic,big room,sci-fi,tutorial,joyful,pads,minimal 170,drill,ethnic 108,amusing,sleepy ambient,psychill,italo disco,lofi,house,acoustic guitar,bassline house,rock,k-pop,synthwave,deep house,electronica,gabber,nightlife,sport & fitness,road trip,celebration,electro,disco house,electronic"
TAG_LIST = TAG_STRING.split(",")

parser = argparse.ArgumentParser(description="Parse da args!!!")

parser.add_argument("-t", "--tags",
    type=str,
    default="",
    help=f"comma separated tags: {TAG_STRING}")

parser.add_argument("-T", "--random-tags",
    metavar="random_tags",
    type=int,
    default=0,
    help=f"add random tags on top of given --tags")

parser.add_argument("-l", "--length",
    type=int,
    default=30,
    help=f"length in seconds")

args = parser.parse_args()

tags = [tag for tag in args.tags.split(",") if tag in TAG_LIST]
for random_tag in [random.choice(TAG_LIST) for i in range(args.random_tags)]:
    tags.append(random_tag)

assert len(tags) > 0, "No Tags found"

email = pat.rand_email()

print(f"Using E-Mail {email}")

pat = pat.get_pat(email)

print(f"Tags: {tags}")

url = generate.get_track_by_tags(tags, pat, args.length)
print(url)
generate.download(url)
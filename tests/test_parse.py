from pba.parse import (Prediction, Response, load_json_to_predictions,
                       parse_file)

FULL_TEST = True

FIRST_PREDICTION = Prediction(
    number=1,
    outcome="right",
    event="PredictionBook will have an Alpha server running by June 20, 2008",
    user="Matt",
    time_created="2008-06-20 03:46:16 UTC",
    time_known="2008-06-20 12:00:00 UTC",
    responses=[Response(user="Matt",
                        time="2008-06-20 03:46:16 UTC",
                        actions={"credence": 80}),
               Response(user="Anonymous",
                        time="2008-08-14 02:28:40 UTC",
                        actions={"outcome": "right"})])

SR_REDANDWHITE = Prediction(
    number=21609,
    outcome="withdrawn",
    event="SR: the user 'redandwhite' was a government agent.",
    user="gwern",
    time_created="2013-10-05 03:17:18 UTC",
    time_known="2016-10-05 03:17:18 UTC",
    responses=[Response(user="gwern",
                        time="2013-10-05 03:17:18 UTC",
                        actions={"credence": 45}),
               Response(user="gwern",
                        time="2016-10-06 17:09:20 UTC",
                        actions={"comment": "remarkably, this is still a mystery. redandwhite was not Force or Banks but there may still have been a third rogue LE agent who could be redandwhite."}),
               Response(user="gwern",
                        time="2016-10-06 17:09:31 UTC",
                        actions={"outcome": "withdrawn"})])

BREXIT_EURO_PARLIAMENT = Prediction(
    outcome="right",
    number=194439,
    event="The Brexit Party to come first in Britain in the 2019 European Parliament elections",
    user="6thNapoleon",
    time_created="2019-02-09 21:01:32 UTC",
    time_known="2019-05-27 08:00:00 UTC",
    responses=[Response(user="6thNapoleon",
                        time="2019-02-09 21:01:32 UTC",
                        actions={"credence": 16}),
               Response(user="6thNapoleon",
                        time="2019-02-09 21:03:54 UTC",
                        actions={"change-prediction": "The Brexit Party to come first in the 2019 European Parliament elections if Britain has extended Article 50 long enough for it to participate",
                                 "change-deadline": "2019-05-26 12:00:00 UTC"}),
               Response(user="6thNapoleon",
                        time="2019-02-09 21:05:23 UTC",
                        actions={"change-prediction": "The Brexit Party to come first (in Britain) in the 2019 European Parliament elections if Article 50 has been extended long enough for Britain to participate",
                                 "change-deadline": "2019-05-26 22:00:00 UTC"}),
               Response(user="pranomostro",
                        actions={"credence": 10},
                        time="2019-02-09 22:06:01 UTC"),
               Response(user="Pablo Stafforini",
                        actions={"credence": 45},
                        time="2019-04-13 17:27:23 UTC"),
               Response(user="Pablo Stafforini",
                        actions={"credence": 62},
                        time="2019-04-17 18:12:52 UTC"),
               Response(user="6thNapoleon",
                        actions={"credence": 82},
                        time="2019-04-22 07:52:03 UTC"),
               Response(user="Pablo Stafforini",
                        actions={"credence": 75},
                        time="2019-05-10 14:51:00 UTC"),
               Response(user="amadeu",
                        actions={"credence": 93},
                        time="2019-05-14 23:08:14 UTC"),
               Response(user="Pablo Stafforini",
                        actions={"credence": 91},
                        time="2019-05-16 12:32:00 UTC"),
               Response(user="Pablo Stafforini",
                        actions={"credence": 96},
                        time="2019-05-16 12:32:20 UTC"),
               Response(user="6thNapoleon",
                        actions={"credence": 98},
                        time="2019-05-16 19:30:05 UTC"),
               Response(user="Baeboo",
                        actions={"credence": 94},
                        time="2019-05-16 22:43:56 UTC"),
               Response(user="stepan",
                        actions={"credence": 10},
                        time="2019-05-22 13:03:08 UTC"),
               Response(user="stepan",
                        actions={"outcome": "right"},
                        time="2019-05-27 08:02:19 UTC")])

DAWN_OF_THE_FINAL_DAY = Prediction(
    number=4934,
    outcome="wrong",
    event="Reddit: “Dawn of The Final Day” meme on frontpage on 2012/12/20.",
    user="muflax",
    time_created="2011-12-20 19:34:55 UTC",
    time_known="2012-12-20 10:06:32 UTC",
    responses=[Response(user="muflax",
                        time="2011-12-20 19:34:55 UTC",
                        actions={"credence": 90}),
               Response(user="muflax",
                        time="2011-12-20 19:35:38 UTC",
                        actions={"comment": '''“number one” is too hard to catch, so just frontpage; see <a href="http://www.reddit.com/r/gaming/comments/njxro/i_going_to_go_ahead_and_predict_that_exactly_one/" rel="nofollow">http://www.reddit.com/r/gaming/comments/njxro/i_going_to_go_ahead_and_predict_that_exactly_one/</a>'''}),
               Response(user="muflax",
                        time="2011-12-20 19:35:53 UTC",
                        actions={"change-deadline": "0201-12-20 11:06:32 UTC"}),
               Response(user="gwern",
                        time="2011-12-20 20:11:20 UTC",
                        actions={"credence": 50,
                                 "comment": "might not be submitted; might not rocket to front page – people might be tired."}),
               Response(user="muflax",
                        time="2012-12-21 09:47:49 UTC",
                        actions={"comment": "didn’t see it; genuinely surprised by that"}),
               Response(user="muflax",
                        time="2012-12-21 09:47:55 UTC",
                        actions={"outcome": "wrong"})])

WORLD_WILL_NOT_END = Prediction(
    number=1377,
    outcome="right",
    event="The world will not end December 25, 2012.",
    user="Houshalter",
    time_created="2010-06-13 15:29:36 UTC",
    time_known="2012-12-26 12:00:00 UTC",
    responses=[Response(user="Houshalter",
                        time="2010-06-13 15:29:36 UTC",
                        actions={"credence": 75}),
               Response(user='maskath@hotmail.com',
                        time="2010-06-19 07:18:38 UTC",
                        actions={"outcome": "right"}),
               Response(user='maskath@hotmail.com',
                        time="2010-06-19 07:18:49 UTC",
                        actions={"outcome": "unknown"}),
               Response(user='maskath@hotmail.com',
                        time="2010-06-19 07:19:04 UTC",
                        actions={"credence": 90}),
               Response(user='ozymandias',
                        time="2010-06-20 19:31:02 UTC",
                        actions={"credence": 99}),
               Response(user='ic9nine',
                        time="2010-06-21 16:23:47 UTC",
                        actions={"outcome": "right"}),
               Response(user='Houshalter',
                        time="2010-06-26 18:57:58 UTC",
                        actions={"outcome": "unknown"}),
               Response(user='Jack',
                        time="2010-07-01 00:34:47 UTC",
                        actions={"credence": 99}),
               Response(user='zuzak',
                        time="2010-07-04 20:33:28 UTC",
                        actions={"credence": 100}),
               Response(user='gwern',
                        time="2010-07-29 08:09:59 UTC",
                        actions={"credence": 100}),
               Response(user='Pavitra',
                        time="2010-08-03 06:23:03 UTC",
                        actions={"credence": 100}),
               Response(user='kallman',
                        time="2010-11-23 02:02:03 UTC",
                        actions={"credence": 100,
                                 "comment": "Wasn’t it supposed to be the 21st anyhow? Only ends for people dead on that date."}),
               Response(user='anonym',
                        time="2010-11-27 20:43:32 UTC",
                        actions={"credence": 100}),
               Response(user='Nic_Smith',
                        time="2010-11-28 00:20:12 UTC",
                        actions={"credence": 100}),
               Response(user='gimpf',
                        time="2010-12-12 17:50:50 UTC",
                        actions={"credence": 100}),
               Response(user='NathanMcKnight',
                        time="2011-11-12 21:53:08 UTC",
                        actions={"credence": 99}),
               Response(user='JoshuaZ',
                        time="2011-11-13 03:54:40 UTC",
                        actions={"credence": 100}),
               Response(user='Isaac',
                        time="2011-11-13 04:00:09 UTC",
                        actions={"credence": 100}),
               Response(user='Anubhav',
                        time="2011-11-13 04:05:17 UTC",
                        actions={"credence": 100}),
               Response(user='bobpage',
                        time="2011-11-13 04:13:37 UTC",
                        actions={"credence": 100}),
               Response(user='RobertLumley',
                        time="2011-11-14 22:15:40 UTC",
                        actions={"credence": 100}),
               Response(user='Jayson Virissimo',
                        time="2011-11-15 10:44:49 UTC",
                        actions={"credence": 100}),
               Response(user='fnedrik',
                        time="2011-11-17 12:38:59 UTC",
                        actions={"credence": 100}),
               Response(user='kilobug',
                        time="2011-11-18 17:04:10 UTC",
                        actions={"credence": 100}),
               Response(user='Tiresias',
                        time="2011-12-20 07:57:36 UTC",
                        actions={"credence": 100}),
               Response(user='lukeprog',
                        time="2012-09-04 02:57:56 UTC",
                        actions={"credence": 100}),
               Response(user='sdr',
                        time="2012-09-13 03:47:19 UTC",
                        actions={"credence": 100}),
               Response(user='Qiaochu',
                        time="2012-11-09 02:48:51 UTC",
                        actions={"credence": 100}),
               Response(user='alecbrooks',
                        time="2012-11-09 06:17:19 UTC",
                        actions={"credence": 100}),
               Response(user='Ken',
                        time="2012-11-12 16:37:45 UTC",
                        actions={"credence": 100}),
               Response(user='Pablo Stafforini',
                        time="2012-11-24 23:59:40 UTC",
                        actions={"credence": 100,
                                 "comment": "Great filter question.  Any answer other than “100” automatically disqualifies someone as a reliable predictor."}),
               Response(user='ygert',
                        time="2012-12-23 18:53:17 UTC",
                        actions={"credence": 100}),
               Response(user='Qiaochu',
                        time="2012-12-26 12:42:42 UTC",
                        actions={"outcome": "right"})])

MARK_ZUCKERBERG_PRESIDENT = Prediction(
    number=180882,
    outcome="unknown",
    event="Mark Zuckerberg will run in the 2020 USA presidential elections.",
    user="Ben Doherty",
    time_created="2017-01-14 00:12:54 UTC",
    time_known="2019-08-16 02:00:00 UTC",
    responses=[Response(user='Ben Doherty',
                        actions={'credence':20},
                        time="2017-01-14 00:12:54 UTC"),
               Response(user="Ben Doherty",
                        actions={'comment': '''@vgr <a href="https://twitter.com/vgr/status/820037536626065408" rel="nofollow">https://twitter.com/vgr/status/820037536626065408</a>, quoting vanity fair <a href="http://www.vanityfair.com/news/2017/01/will-mark-zuckerberg-be-our-next-president" rel="nofollow">http://www.vanityfair.com/news/2017/01/will-mark-zuckerberg-be-our-next-president</a>'''},
                        time="2017-01-14 00:14:10 UTC"),
               Response(user="Ben Doherty",
                        time="2017-01-14 00:16:02 UTC",
                        actions={'made-visible': None}),
               Response(user='themusicgod1',
                        actions={'credence':17},
                        time="2017-01-14 02:42:32 UTC"),
               Response(user='LKBM',
                        actions={'credence':2},
                        time="2017-01-16 02:21:20 UTC"),
               Response(user='penten',
                        actions={'credence':5},
                        time="2017-01-16 08:53:03 UTC"),
               Response(user='splorridge',
                        actions={'credence':5},
                        time="2017-01-16 13:57:41 UTC"),
               Response(user='RandomThinker',
                        actions={'credence':10,
                                 'comment': 'Sometimes hard to say what “run” means.  He might explore, and we’ll never know.'},
                        time="2017-01-16 20:19:01 UTC"),
               Response(user='RandomThinker',
                        actions={'comment': '''I prefer this one.  <a href="http://predictionbook.com/predictions/180935" rel="nofollow">http://predictionbook.com/predictions/180935</a>'''},
                        time="2017-01-16 20:19:38 UTC"),
               Response(user="Faceh",
                        time="2017-01-17 17:04:37 UTC",
                        actions={'credence': 5,
                                 'comment': 'Main issue is “Presidential” elections. Little reason to think he will go straight for that rather than, say, Governor or Senator. The question of whether he will run for ANY state or higher political office in the next 4 years is more interesting.'}),
               Response(user='Afforess',
                        actions={'credence':10},
                        time="2017-01-20 17:57:00 UTC"),
               Response(user='jasticE',
                        actions={'credence':5},
                        time="2017-01-21 22:12:08 UTC"),
               Response(user='jasticE',
                        actions={'credence':2},
                        time="2017-01-21 22:26:52 UTC"),
               Response(user='pent',
                        actions={'credence':5},
                        time="2017-01-23 22:58:43 UTC"),
               Response(user='Jayson Virissimo',
                        actions={'credence':5},
                        time="2017-01-23 23:02:50 UTC"),
               Response(user='ioannes',
                        actions={'credence':5},
                        time="2017-01-25 18:23:44 UTC"),
               Response(user='Faceh',
                        actions={'credence':20,
                                 'comment': 'He has been making an nationwide road trip, which increases chances he is running for a popularly elected office…'},
                        time="2017-07-07 00:33:32 UTC"),
               Response(user='timmartin',
                        actions={'credence':2},
                        time="2017-11-19 09:28:31 UTC"),
               Response(user='JoshuaZ',
                        actions={'credence':22},
                        time="2017-11-19 14:57:35 UTC"),
               Response(user='Baeboo',
                        actions={'credence':20},
                        time="2017-11-21 05:46:52 UTC"),
               Response(user='Baeboo',
                        actions={'credence':23},
                        time="2017-12-02 04:44:20 UTC"),
               Response(user='JoshuaZ',
                        actions={'credence':12},
                        time="2017-12-02 19:38:15 UTC"),
               Response(user='objclone',
                        actions={'credence':5},
                        time="2017-12-03 04:16:35 UTC"),
               Response(user='Baeboo',
                        actions={'credence':18},
                        time="2018-01-14 09:00:30 UTC"),
               Response(user='peter_hurford',
                        actions={'credence':10},
                        time="2018-01-15 00:30:36 UTC"),
               Response(user='Baeboo',
                        actions={'credence':16},
                        time="2018-02-07 18:00:30 UTC"),
               Response(user='davatk',
                        actions={'credence':3},
                        time="2018-04-24 05:39:27 UTC"),
               Response(user='JTPeterson',
                        actions={'credence':1},
                        time="2018-04-24 16:18:14 UTC"),
               Response(user='pranomostro',
                        actions={'credence':40},
                        time="2018-12-08 23:04:50 UTC"),
               Response(user='6thNapoleon',
                        actions={'credence':2},
                        time="2019-01-30 19:37:32 UTC"),
               Response(user='aarongertler',
                        actions={'credence':0},
                        time="2019-01-30 21:59:08 UTC"),
               Response(user='Baeboo',
                        actions={'credence':4},
                        time="2019-02-01 02:42:53 UTC"),
               Response(user='Cato',
                        actions={'credence':1},
                        time="2019-02-01 08:26:55 UTC"),
               Response(user='Cato',
                        actions={'credence':0},
                        time="2019-02-18 07:32:16 UTC")])

KOREAN_WAR = Prediction(
    outcome="wrong",
    event='War between North and South Korea breaks out by Jan 1, 2016',
    user='themusicgod1',
    time_created='2015-12-11 06:34:25+00:00',
    time_known='2016-01-01 12:00:00+00:00',
    number=175191,
    responses=[Response(user='themusicgod1',
                        time='2015-12-11 06:34:25 UTC',
                        actions={'credence': 0}),
               Response(user='Medea',
                        time='2015-12-11 10:35:45 UTC',
                        actions={'credence': 2}),
               Response(user='JoshuaZ',
                        time='2015-12-11 11:47:15 UTC',
                        actions={'credence': 0}),
               Response(user='bobpage',
                        time='2015-12-11 17:55:00 UTC',
                        actions={'comment': '&lt; 0.05 % ',
                                 'credence': 1}),
               Response(user='kuudes',
                        time='2015-12-17 23:15:04 UTC',
                        actions={'comment': 'Technically, they are currently at war with only temporary ceasefire, so I am uncertain how this will be judged?'}),
               Response(user='JoshuaZ',
                        time='2015-12-18 01:52:59 UTC',
                        actions={'comment': 'I presume something with a lot more shooting such that everyone refers to it as a war? That’s at least how I interpreted it. '}),
               Response(user='themusicgod1',
                        time='2015-12-18 07:16:20 UTC',
                        actions={'comment': '@Kuudes that is correct, afaik they are in a state of war but I was thinking something bigger and should have probably clarified.  At least 1 missile landing in Seoul or equivalent damage to north/south korea followed by either immediate peace talks'}),
               Response(user='themusicgod1',
                        time='2015-12-18 07:16:38 UTC',
                        actions={'comment': 'or over 1000 casualties would suffice',
                                 'credence': 0}),
               Response(user='themusicgod1',
                        time='2015-12-18 07:16:51 UTC',
                        actions={'credence': 0}),
               Response(user='Raahul_Kumar',
                        time='2015-12-20 03:24:40 UTC',
                        actions={'credence': 0}),
               Response(user='themusicgod1',
                        time='2015-12-31 22:44:10 UTC',
                        actions={'outcome': 'wrong'}),
               Response(user='themusicgod1',
                        time='2015-12-31 22:44:34 UTC',
                        actions={'comment': 'jan 1 in korea'})])

HPMOR_SNAPE = Prediction(
    number=6477,
    outcome="wrong",
    event="HP MoR: Cloak & Hat is Severus Snape",
    user="gwern",
    time_created="2012-04-08 18:27:35 UTC",
    time_known="2015-01-01 12:00:00 UTC",
    responses=[Response(user="gwern",
                        actions={'credence': 20},
                        time="2012-04-08 18:27:35 UTC"),
               Response(user="ahartell",
                        actions={'credence': 10},
                        time="2012-04-09 04:55:30 UTC"),
               Response(user="PlacidPlatypus",
                        actions={'credence': 20},
                        time="2012-04-19 05:20:43 UTC"),
               Response(user="disinter",
                        actions={'credence': 40},
                        time="2012-04-20 02:39:43 UTC"),
               Response(user="Oscar_Cunningham",
                        actions={'credence': 20},
                        time="2012-04-20 11:48:28 UTC"),
               Response(user="Flailingjunk",
                        actions={'credence': 60},
                        time="2012-04-23 07:22:52 UTC"),
               Response(user="Flailingjunk",
                        actions={'credence': 80},
                        time="2012-09-21 05:34:48 UTC"),
               Response(user="PlacidPlatypus",
                        actions={'outcome': 'wrong'},
                        time="2015-03-20 18:39:24 UTC")])


TEST_PREDICTIONS = [FIRST_PREDICTION, SR_REDANDWHITE, BREXIT_EURO_PARLIAMENT, DAWN_OF_THE_FINAL_DAY,
                    WORLD_WILL_NOT_END, KOREAN_WAR, MARK_ZUCKERBERG_PRESIDENT, HPMOR_SNAPE]

if FULL_TEST:
    JSON_FILE = "data/predictions.json"
    ALL_PREDICTIONS = load_json_to_predictions(JSON_FILE)


def prediction_diff(p1, p2):
    if p1.user != p2.user:
        print("user: ", p1.user, "!=", p2.user)
    if p1.event != p2.event:
        print("event: ", p1.event, "!=", p2.event)
    if p1.outcome != p2.outcome:
        print("outcome: ", p1.outcome, "!=", p2.outcome)
    if p1.time_created != p2.time_created:
        print("time_created: ", p1.time_created, "!=", p2.time_created)
    if p1.time_known != p2.time_known:
        print("time_known: ", p1.time_known, "!=", p2.time_known)
    if p1.number != p2.number:
        print("number: ", p1.number, "!=", p2.number)
    responses_diff(p1.responses, p2.responses)


def responses_diff(rs1, rs2):
    for r1, r2 in zip(rs1, rs2):
        if r1 != r2:
            print("Response diff:")
        if r1.user != r2.user:
            print("\tuser: ", r1.user, "!=", r2.user)
        if r1.time != r2.time:
            print("\ttime: ", r1.time, "!=", r2.time)
        if r1.actions != r2.actions:
            print("\tActions diff:")
            for (act_type1, act1), (act_type2, act2) in zip(sorted(r1.actions.items()),
                                                            sorted(r2.actions.items())):
                if act_type1 != act_type2:
                    print(f"\t\ttype: {act_type1} -> {act_type2}")
                if act1 != act2:
                    print(f"\t\tvalue: {act1} -> {act2}")


def test_treat_404_correctly():
    assert parse_file("data/pages/page-175193.html") is None


def test_parse_file():
    for prediction in TEST_PREDICTIONS:
        assert parse_file(f"data/test-pages/page-{prediction.number}.html") == prediction


def test_prediction_roundtrip_serialize():
    '''
    Make sure to_dict() and from_dict() compose to identity.
    '''
    for prediction in TEST_PREDICTIONS:
        assert Prediction.from_dict(prediction.to_dict()) == prediction


def test_no_empty_fields():
    if not FULL_TEST:
        return True
    for prediction in ALL_PREDICTIONS:
        fields = [prediction.number, prediction.event, prediction.outcome,
                  prediction.user, prediction.time_created, prediction.time_known,
                  prediction.responses]
        assert None not in fields
        assert "" not in fields
        assert [] not in fields

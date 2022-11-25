from Domain.Entities.Tip import Tip

tip1_no_media_ok = Tip(
    tipster_id= "111",
    match_id= "222",
    analysis= "Barcelona will win because Barcelona tiene poder",
    bookie_id= "333",
    rate= 1.80,
    stake= 4.50,
    pick_id= "fc_barcelona",
    media= {"items":[]}
)

tip2_media_ok = Tip(
    tipster_id= "111",
    match_id= "229",
    analysis= "Rafa Nadal is best boi",
    bookie_id= "339",
    rate= 1.80,
    stake= 4.50,
    pick_id= "nadal_rafael",
    media= {"items":["banana1.txt", "banana2.txt", "banana3.txt"]}
)

tip3_other_tipster_ok = Tip(
    tipster_id= "222",
    match_id= "229",
    analysis= "Rafa Nadal is best boi",
    bookie_id= "339",
    rate= 1.80,
    stake= 4.50,
    pick_id= "nadal_rafael",
    media= {"items":[]}
)

tip4_same_tipster_and_match_fail = Tip(
    tipster_id= "111",
    match_id= "222",
    analysis= "Actually, Madrid is better",
    bookie_id= "333",
    rate= 1.80,
    stake= 4.50,
    pick_id= "fc_barcelona",
    media= {"items":[]}
)

tip5_no_tipster_fail = {
    "tipster_id": "",
    "match_id": "222",
    "analysis": "Barcelona will win because Barcelona tiene poder",
    "bookie_id": "444",
    "rate": 1.80,
    "stake": 4.50,
    "pick_id": "fc_barcelona",
    "media": {"items":[]}
}

tip6_too_many_media_fail = {
    "tipster_id": "aaa",
    "match_id": "222",
    "analysis": "Barcelona will win because Barcelona tiene poder",
    "bookie_id": "444",
    "rate": 1.80,
    "stake": 4.50,
    "pick_id": "fc_barcelona",
    "media": {"items":["1", "2", "3", "4", "5", "6"]}
}

tip7_too_large_stake_fail = {
    "tipster_id": "aaa",
    "match_id": "222",
    "analysis": "Barcelona will win because Barcelona tiene poder",
    "bookie_id": "444",
    "rate": 1.80,
    "stake": 88.0,
    "pick_id": "fc_barcelona",
    "media": {"items":["1", "2"]}
}
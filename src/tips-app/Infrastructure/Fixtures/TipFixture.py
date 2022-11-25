from Domain.Entities.Tip import Tip

mock_tip1_ok = Tip(
    tipster_id= "111",
    match_id= "222",
    analysis= "Barcelona will win because Barcelona tiene poder",
    bookie_id= "333",
    rate= 1.80,
    stake= 4.50,
    pick_id= "fc_barcelona",
    media= {"items":[]}
)

mock_tip2_ok = Tip(
    tipster_id= "111",
    match_id= "229",
    analysis= "Rafa Nadal is best boi",
    bookie_id= "339",
    rate= 1.80,
    stake= 4.50,
    pick_id= "nadal_rafael",
    media= {"items":["banana1.txt", "banana2.txt", "banana3.txt"]}
)

mock_tip3_ok = Tip(
    tipster_id= "222",
    match_id= "229",
    analysis= "Rafa Nadal is best boi",
    bookie_id= "339",
    rate= 1.80,
    stake= 4.50,
    pick_id= "nadal_rafael",
    media= {"items":["banana1.txt", "banana2.txt", "banana3.txt"]}
)

mock_tip3_fail = Tip(
    tipster_id= "111",
    match_id= "222",
    analysis= "Actually, Madrid is better",
    bookie_id= "333",
    rate= 1.80,
    stake= 4.50,
    pick_id= "fc_barcelona",
    media= {"items":[]}
)

mock_tip4_fail = {
    "tipster_id": "",
    "match_id": "222",
    "analysis": "Barcelona will win because Barcelona tiene poder",
    "bookie_id": "444",
    "rate": 1.80,
    "stake": 4.50,
    "pick_id": "fc_barcelona",
    "media": {"items":[]}
}

mock_tip5_fail = {
    "tipster_id": "aaa",
    "match_id": "222",
    "analysis": "Barcelona will win because Barcelona tiene poder",
    "bookie_id": "444",
    "rate": 1.80,
    "stake": 4.50,
    "pick_id": "fc_barcelona",
    "media": {"items":["1", "2", "3", "4", "5", "6"]}
}

mock_tip6_fail = {
    "tipster_id": "aaa",
    "match_id": "222",
    "analysis": "Barcelona will win because Barcelona tiene poder",
    "bookie_id": "444",
    "rate": 1.80,
    "stake": 88.0,
    "pick_id": "fc_barcelona",
    "media": {"items":["1", "2"]}
}
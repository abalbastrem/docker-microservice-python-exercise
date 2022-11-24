from Domain.Entities.Tip import Tip

mock_tip1_ok = Tip(
    tipster_id= "111",
    match_id= "222",
    analysis= "Barça will win because Barça is good",
    bookie_id= "333",
    rate= 1.80,
    stake= 4.50,
    pick_id= "fc_barcelona",
    media= {"items":["mediafile.jpg"]}
)

mock_tip2_ok = Tip(
    tipster_id= "111",
    match_id= "229",
    analysis= "Rafa Nadal is best boi",
    bookie_id= "339",
    rate= 1.80,
    stake= 4.50,
    pick_id= "nadal_rafael",
    media= {"items":[]}
)

mock_tip3_fail = Tip(
    tipster_id= "111",
    match_id= "222",
    analysis= "Actually, Madrid is better",
    bookie_id= "333",
    rate= 1.80,
    stake= 4.50,
    pick_id= "fc_barcelona",
    media= {"items":[".mediafile.jpg",
            "mediafile2.jpg"]}
)

mock_tip4_fail = Tip(
    tipster_id= "",
    match_id= "222",
    analysis= "Barça will win because Barça is good",
    bookie_id= "444",
    rate= 1.80,
    stake= 4.50,
    pick_id= "fc_barcelona",
    media= {"items":[]}
)
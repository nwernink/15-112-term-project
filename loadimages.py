def loadImages(app):
    # load images and initiate their variables
    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.iconfinder.com%2Ficons%2F3984453%2Fcasino_croupier_dealer_gambling_staff_icon&psig=AOvVaw31O6C1OK8N0_PyxzvXSEPa&ust=1619042755117000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOj15rfqjfACFQAAAAAdAAAAABAG
    app.dealerImage = app.loadImage('dealer.png')
    app.dealerScaledImage = app.scaleImage(app.dealerImage, 1/3)
    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.kindpng.com%2Fimgv%2FTRmJRRm_royal-flush-cards-png-spade-royal-flush-transparent%2F&psig=AOvVaw3Bk6Wf4xyz-VqfoE2HybFW&ust=1619042820249000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJDLiNXqjfACFQAAAAAdAAAAABAD
    app.pokerImage = app.loadImage('poker.png')
    app.pokerScaledImage = app.scaleImage(app.pokerImage, 1/2)
    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.beatblackjack.org%2F&psig=AOvVaw0yeh_bYbmW4IYtPbjvT376&ust=1619042848385000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCMjN6OHqjfACFQAAAAAdAAAAABAK
    app.blackjackImage = app.loadImage('blackjack.png')
    app.blackjackScaledImage = app.scaleImage(app.blackjackImage, 1)
    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.clipartkey.com%2Fview%2FhToxwo_casino-roulette-png-clip-art-roulette-wheel-clipart%2F&psig=AOvVaw3Ov2SBBL_26g3ZHgZhwHdi&ust=1619042878549000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCMC62PLqjfACFQAAAAAdAAAAABAD
    app.rouletteImage = app.loadImage('roulette.jpg')
    app.rouletteScaledImage = app.scaleImage(app.rouletteImage, 1)
    # https://www.google.com/url?sa=i&url=https%3A%2F%2Femojiisland.com%2Fproducts%2Fnerd-with-glasses-emoji-icon&psig=AOvVaw26attj8j7HsJLSY-IrMsrI&ust=1619042664708000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKi_l4vqjfACFQAAAAAdAAAAABAK
    app.you = app.loadImage('you.png')
    app.youScaled = app.scaleImage(app.you,1/8)

    # load images for cpu and initiate their variables (all credit to @koz!)
    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.conference-board.org%2Fblog%2Fauthor%2Fdavi-kosbie&psig=AOvVaw3E1hMWbm6yveFJrS6FcqbP&ust=1619042385637000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJCb2JnpjfACFQAAAAAdAAAAABAI
    app.cpu1 = app.loadImage('koz1.png')
    app.cpu1Scaled = app.scaleImage(app.cpu1, 1/7)
    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DsFlrl-bTSQ8&psig=AOvVaw3E1hMWbm6yveFJrS6FcqbP&ust=1619042385637000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJCb2JnpjfACFQAAAAAdAAAAABAO
    app.cpu2 = app.loadImage('koz2.png')
    app.cpu2Scaled = app.scaleImage(app.cpu2, 1/3.7)
    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DY7s5rxhbNJM&psig=AOvVaw3E1hMWbm6yveFJrS6FcqbP&ust=1619042385637000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJCb2JnpjfACFQAAAAAdAAAAABAU
    app.cpu3 = app.loadImage('koz3.png')
    app.cpu3Scaled = app.scaleImage(app.cpu3, 1/5.5)
    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fthetartan.org%2F2014%2F2%2F17%2Fnews%2Fmortarboard&psig=AOvVaw3E1hMWbm6yveFJrS6FcqbP&ust=1619042385637000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJCb2JnpjfACFQAAAAAdAAAAABAa
    app.cpu4 = app.loadImage('koz4.png')
    app.cpu4Scaled = app.scaleImage(app.cpu4, 1/5)
    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.shadysideacademy.org%2Fabout%2Fnews%2Fnews-post%2F~post%2Fhour-of-code-3d-design-and-speaker-highlight-computer-science-education-week-20181213&psig=AOvVaw3E1hMWbm6yveFJrS6FcqbP&ust=1619042385637000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJCb2JnpjfACFQAAAAAdAAAAABAg
    app.cpu5 = app.loadImage('koz5.png')
    app.cpu5Scaled = app.scaleImage(app.cpu5, 1/4.2)
    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.kosbie.net%2Fcmu%2F&psig=AOvVaw3E1hMWbm6yveFJrS6FcqbP&ust=1619042385637000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJCb2JnpjfACFQAAAAAdAAAAABAl
    app.cpu6 = app.loadImage('koz6.png')
    app.cpu6Scaled = app.scaleImage(app.cpu6, 1/13)
    # https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.cs.cmu.edu%2Fnews%2Foutstanding-contributions-scs-recognized-founders-day&psig=AOvVaw3E1hMWbm6yveFJrS6FcqbP&ust=1619042385637000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJCb2JnpjfACFQAAAAAdAAAAABAp
    app.cpu7 = app.loadImage('koz7.png')
    app.cpu7Scaled = app.scaleImage(app.cpu7, 1/3.8)
import speedtest


def test():
    s = speedtest.Speedtest()
    s.get_server()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.result.dict()
    return res["download"], res["upload"], res["ping"]


def  main():

   for i in range(3):
       d,u,p=test()

   print("Viteza de descarcare wifi".format(d/1024))
   print("Viteza de incarcare wifi".format(u/1024))
   print("Ping".format(p))

if __name__ == "__main__":
    main()
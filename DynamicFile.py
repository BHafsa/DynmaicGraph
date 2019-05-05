
import pandas as  pd
import sys

def main(argv):
    df = pd.read_csv(argv[1]+'.txt',sep=',')
    df.columns =['src','dst','timestemps']
    df=df.sort_values('timestemps')
    #df=df.set_index('timestemps')
    out = pd.DataFrame([])
    #out.columns =['src','dst','timestemps']
    ancien = df.iloc[0].timestemps
    df_ancien =pd.DataFrame()
    for time,row in df.iterrows():
        print(time)
        if(ancien != row.timestemps):
            out  = out.append(df_ancien)
            df_ancien['1'] = row.timestemps
            ancien = row.timestemps
        df_ancien= df_ancien.append({'1':row['timestemps'],'2':row['src'],'3':row['dst']},ignore_index=True)
    
    df_ancien['1'] = df.iloc[-1].timestemps
   
    out=out.append(df_ancien)
    out= out.drop_duplicates()
    out=out.astype({'1':'int64','2':'int64','3':'int64'})
    out = out[['2','3','1']]
    
    out.to_csv(argv[1]+"_out.txt",sep=' ',index=False)

if __name__ == "__main__":
    main(sys.argv)
import pandas as pd
from csv import writer

# df=pd.read_csv('IYCF.csv')
#
# cols=list(df.columns)   #list of all columns in csv
# micro_list=[]          #list of micro nutrients in csv
# for i in range(2,len(cols),3):
#     micro_list.append(cols[i])
# print(len(micro_list))
# fin_val={}   #dictionary to be returned
# for i in micro_list:
#     fin_val[i]=0
# print(fin_val)

recipe={
    'ground nut':1,

}

# dish_name='Green gram curry'
dish_name=['Grenn gram curry','Paneer masala','Jowar soya dosa with sesame seed powder']
def get_recipe(dish_name):
    for i in range(len(dish_name)):
        dish_name[i] = dish_name[i].lower()
    # dish_name=dish_name.lower()
    recipe={}
    dfr=pd.read_csv('recipe.csv')
    df=dfr.copy()
    df['ingredient'] = df['ingredient'].str.strip()
    df['recipe'] = df['recipe'].str.strip()
    df['ingredient'] = df['ingredient'].str.lower()
    df['recipe'] = df['recipe'].str.lower()
    if dish_name[i] in df['recipe'].values:
        for ind in df.index:
            if df['recipe'][ind]==dish_name[i]:
                if df['measurement'][ind]=='g':
                    recipe[df['ingredient'][ind]]=df['quantity'][ind]/100
                elif df['measurement'][ind]=='tsp':
                    recipe[df['ingredient'][ind]]=df['quantity'][ind]*4.5/100
                elif df['measurement'][ind] == 'tbsp':
                    recipe[df['ingredient'][ind]] = df['quantity'][ind] * 13.5 / 100
                elif df['measurement'][ind] == 'cup':
                    recipe[df['ingredient'][ind]] = df['quantity'][ind] * 120 / 100
                elif df['measurement'][ind] == 'no':
                    recipe[df['ingredient'][ind]] = df['quantity'][ind]
    else:
        print(dish_name+ ' not in recipe list')
        data=[[dish_name]]
        dataframe = pd.DataFrame(data)
        dataframe.to_csv("recipe_missing.csv", index=False, mode='a', header=False)
    return recipe
# applying whitespace_remover function on dataframe

print(get_recipe(dish_name))
# printing dataframe

# food_name=recipe.keys()
# print(food_name)

def cal(recipe):
    dfd = pd.read_csv('IYCF.csv')
    df=dfd.copy()

    cols = list(df.columns)  # list of all columns in csv
    micro_list = []  # list of micro nutrients in csv
    for i in range(2, len(cols), 3):
        micro_list.append(cols[i])
        df[cols[i-1]]=df[cols[i-1]].str.strip()
        df[cols[i - 1]] = df[cols[i - 1]].str.lower()
    print(len(micro_list))
    fin_val = {}  # dictionary to be returned
    for i in micro_list:
        fin_val[i] = 0
   # print(fin_val)
    food_name = recipe.keys()
    print(food_name)
    for i in range(1, len(cols), 3):
        for j in food_name:
            if j in df[cols[i]].values:
                print('yes')
                val = int(df[df[cols[i]] == j][cols[i + 1]])
                val = val * recipe[j]
                fin_val[cols[i + 1]] += val
                print(val)
            else:
                print('no')
                data = [ [j,cols[i+1]],]
                # with open('ingredient_missing.csv', 'a') as f_object:
                #     writer_object = writer(f_object)
                #     writer_object.writerow(data)
                #     f_object.close()
                dataframe = pd.DataFrame(data)
                dataframe.to_csv("ingredient_missing.csv", index=False, mode='a', header=False)
    return fin_val

print(cal(get_recipe(dish_name)))



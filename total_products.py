from tkinter import *
import sqlite3



root = Tk()
root.title("Total Products App")
root.geometry("780x700")
root.config(background="#D9F7F4")
icon = PhotoImage(file="workers.logo.png")
root.iconphoto(True, icon)


title_label = Label(root, text="ΣΥΝΟΛΙΚΑ ΑΓΡΟΤΙΚΑ ΠΡΟΙΟΝΤΑ \nΕΣΟΔΑ ΚΑΙ ΕΞΟΔΑ", font=("arial black", 14), background="black", foreground="#3AF10A", relief="ridge", borderwidth=7)
title_label.grid(row=0, columnspan=2, pady=(5, 30), ipadx=10, ipady=10)

def total_all_kilos():
    global total_all_kilos_label

    conn = sqlite3.connect("kastana_file.db")
    c = conn.cursor()

    c.execute("SELECT SUM(extra_size_kilos + a_size_kilos + b_size_kilos + c_size_kilos + torn_kilos) FROM products")
    result = c.fetchone()[0]
    total_all_kilos_value = 0 if result is None else int(result)

    total_all_kilos_label.config(text="ΣΥΝΟΛΙΚΑ  ΚΙΛΑ  : {} ".format(total_all_kilos_value))


def calculate_total_kilo_k():
    conn = sqlite3.connect("cherries_file.db")
    c = conn.cursor()
    c.execute("SELECT SUM(kilo_k) FROM products")
    total = c.fetchone()[0]
    if total is None:
        total = 0
    total_kilo_k_label.config(text="ΣΥΝΟΛΙΚΑ ΚΙΛΑ  : {} ".format(total))



def total_all_euros():
    global total_all_euros_label
    conn = sqlite3.connect("kastana_file.db")
    c = conn.cursor()

    c.execute("SELECT extra_size_kilos, extra_size_price, a_size_kilos, a_size_price, b_size_kilos, b_size_price, c_size_kilos, c_size_price, torn_kilos, torn_price FROM products")
    rows = c.fetchall()
    total_all_euros = 0

    for row in rows:
        extra_kilos = row[0]
        extra_price = row[1]
        a_kilos = row[2]
        a_price = row[3]
        b_kilos = row[4]
        b_price = row[5]
        c_kilos = row[6]
        c_price = row[7]
        torn_kilos = row[8]
        torn_price = row[9]

        if extra_kilos and extra_price and extra_kilos.strip() and extra_kilos.strip() != 'ΚΙΛΑ':
            extra_kilos = float(''.join(filter(str.isdigit, extra_kilos)))
            if extra_price.strip() and extra_price.strip() != '€':
                extra_price = float(str(extra_price).replace(',', '.').replace('€', ''))
                total_all_euros += extra_kilos * extra_price

        if a_kilos and a_price and a_kilos.strip() and a_kilos.strip() != 'ΚΙΛΑ':
            a_kilos = float(''.join(filter(str.isdigit, a_kilos)))
            if a_price.strip() and a_price.strip() != '€':
                a_price = float(str(a_price).replace(',', '.').replace('€', ''))
                total_all_euros += a_kilos * a_price

        if b_kilos and b_price and b_kilos.strip() and b_kilos.strip() != 'ΚΙΛΑ':
            b_kilos = float(''.join(filter(str.isdigit, b_kilos)))
            if b_price.strip() and b_price.strip() != '€':
                b_price = float(str(b_price).replace(',', '.').replace('€', ''))
                total_all_euros += b_kilos * b_price

        if c_kilos and c_price and c_kilos.strip() and c_kilos.strip() != 'ΚΙΛΑ':
            c_kilos = float(''.join(filter(str.isdigit, c_kilos)))
            if c_price.strip() and c_price.strip() != '€':
                c_price = float(str(c_price).replace(',', '.').replace('€', ''))
                total_all_euros += c_kilos * c_price

        if torn_kilos and torn_price and torn_kilos.strip() and torn_kilos.strip() != 'ΚΙΛΑ':
            torn_kilos = float(''.join(filter(str.isdigit, torn_kilos)))
            if torn_price.strip() and torn_price.strip() != '€':
                torn_price = float(str(torn_price).replace(',', '.').replace('€', ''))
                total_all_euros += torn_kilos * torn_price

    conn.close()

    total_all_euros_label.config(text="ΣΥΝΟΛΟ ΕΥΡΩ : {:.2f} €".format(total_all_euros))
    return total_all_euros


def calculate_total_euro():
    conn = sqlite3.connect("cherries_file.db")
    c = conn.cursor()

    c.execute("SELECT kilo_k, price FROM products")
    rows = c.fetchall()
    total_euro = sum(
        float(''.join(filter(str.isdigit, row[0]))) * float(str(row[1]).replace(',', '.')) for row in rows if
        row[0] and row[1])

    conn.close()
    total_euro_label.config(text="ΣΥΝΟΛΟ ΕΥΡΩ : {:.2f} €".format(total_euro))

    return total_euro


def total_cost_workers():
    conn = sqlite3.connect("workers_cost_file.db")
    c = conn.cursor()

    c.execute("SELECT price FROM workers")
    rows = c.fetchall()
    total_euros = sum(
        float(str(row[0]).replace(',', '.')) for row in rows if
        row[0])

    conn.close()
    total_cost_label.config(text="ΣΥΝΟΛΟ ΕΥΡΩ : {:.2f} €".format(total_euros))

    return total_euros


def total_euros():
    conn = sqlite3.connect("pesticide_and_fertilizers_file.db")
    c = conn.cursor()

    c.execute("SELECT price FROM products")
    rows = c.fetchall()
    total_euros = sum(
        float(str(row[0]).replace(',', '.')) for row in rows if
        row[0])

    conn.close()
    total_euros_label.config(text="ΣΥΝΟΛΟ ΕΥΡΩ : {:.2f} €".format(total_euros))

    return total_euros


def total_all_total():
    total_all_euros = float(total_all_euros_label["text"].split(":")[1].strip().split(" ")[0])
    calculate_total_euro = float(total_euro_label["text"].split(":")[1].strip().split(" ")[0])
    total_cost_workers = float(total_cost_label["text"].split(":")[1].strip().split(" ")[0])
    total_euros = float(total_euros_label["text"].split(":")[1].strip().split(" ")[0])

    total_profit = total_all_euros + calculate_total_euro - total_cost_workers - total_euros
    total_all_total_label.config(text="ΣΥΝΟΛΙΚΟ ΚΕΡΔΟΣ : {:.2f} €".format(total_profit))





total_all_kilos_label = Label(root, text=" ", font=("arial black", 13), foreground="#5105B4", background="#F0EBD8", relief="ridge", borderwidth=5, width=30)
total_all_kilos_label.grid(row=1, column=1, padx=10, pady=10)

total_kilo_k_label = Label(root, text=" ", font=("arial black", 13), foreground="#5105B4", background="#F0EBD8", relief="ridge", borderwidth=5, width=30)
total_kilo_k_label.grid(row=2, column=1, padx=10, pady=10)


total_all_euros_label = Label(root, text=" ", font=("arial black", 13), foreground="#5105B4", background="#F0EBD8", relief="ridge", borderwidth=5, width=30)
total_all_euros_label.grid(row=3, column=1, padx=10, pady=10)

total_euro_label = Label(root, text=" ", font=("arial black", 13), foreground="#5105B4", background="#F0EBD8", relief="ridge", borderwidth=5, width=30)
total_euro_label.grid(row=4, column=1, padx=10, pady=10)

total_cost_label = Label(root, text=" ", font=("arial black", 13), foreground="#5105B4", background="#F0EBD8", relief="ridge", borderwidth=5, width=30)
total_cost_label.grid(row=5, column=1, padx=10, pady=10)

total_euros_label = Label(root, text=" ", font=("arial black", 13), foreground="#5105B4", background="#F0EBD8", relief="ridge", borderwidth=5, width=30)
total_euros_label.grid(row=6, column=1, padx=10, pady=10)

total_all_total_label = Label(root, text=" ", font=("arial black", 14), background="#F0EBD8", foreground="#360577", relief="ridge", borderwidth=6, width=35)
total_all_total_label.grid(row=8, columnspan=2, pady=5)




chestnuts_btn = Button(root, text="ΚΑΣΤΑΝΑ ΣΥΝΟΛΙΚΑ ΚΙΛΑ", font=("arial black", 12), bd=4, width=20, command=total_all_kilos, background="#E1AA08")
chestnuts_btn.grid(row=1, column=0, ipadx=50, pady=10)

cherries_btn = Button(root, text="ΚΕΡΑΣΙΑ ΣΥΝΟΛΙΚΑ ΚΙΛΑ", font=("arial black", 12), bd=4, width=20, command=calculate_total_kilo_k, background="#E1AA08")
cherries_btn.grid(row=2, column=0, ipadx=50, pady=10)



chestnuts1_btn = Button(root, text="ΚΑΣΤΑΝΑ ΣΥΝΟΛΙΚΑ ΕΥΡΩ", font=("arial black", 12), bd=4, width=20, command=total_all_euros, background="#E1AA08")
chestnuts1_btn.grid(row=3, column=0, ipadx=50, pady=10, padx=10)

cherries1_btn = Button(root, text="ΚΕΡΑΣΙΑ ΣΥΝΟΛΙΚΑ ΕΥΡΩ", font=("arial black", 12), bd=4, width=20, command=calculate_total_euro, background="#E1AA08")
cherries1_btn.grid(row=4, column=0, ipadx=50, pady=10)

workers_btn = Button(root, text="ΚΟΣΤΟΣ ΕΡΓΑΤΩΝ", font=("arial black", 12), bd=4, width=23, command=total_cost_workers, background="#E1AA08")
workers_btn.grid(row=5, column=0, ipadx=31, pady=10)

pesticide_btn = Button(root, text="ΦΥΤΟΦΑΡΜΑΚΑ ΚΑΙ ΛΙΠΑΣΜΑΤΑ", font=("arial black", 12), bd=4, width=23, command=total_euros, background="#E1AA08")
pesticide_btn.grid(row=6, column=0, ipadx=32, pady=10)

total_all_total_btn = Button(root, text="ΣΥΝΟΛΙΚΟ ΚΕΡΔΟΣ", font=("arial black", 14), bd=5, command=total_all_total, background="#03B20A")
total_all_total_btn.grid(row=7, columnspan=2, ipadx=50, pady=20)

name_label = Label(root, text="Created and Designed by : Papaioannou Antonios", font=("arial black", 10), foreground="grey", background="#D9F7F4", borderwidth=1)
name_label.grid(column=0, row=9, sticky=E, pady=(5, 0))



root.mainloop()
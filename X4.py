rint('Vertical Histogram')
print("Progress", "Trailer", "Retriever","Exclude")
for x in range(max(progress,module_trailer,module_retriever,exclude)):
    print("   {0}        {1}        {2}       {3}".format(
                "*" if x < progress else " ",
                "*" if x < module_trailer else " ",
                "*" if x < module_retriever else " ",
                "*" if x < exclude else " "))

for file in * 
    do
        git add $file
        git commit -m "backend integration"
        git push
    done

    
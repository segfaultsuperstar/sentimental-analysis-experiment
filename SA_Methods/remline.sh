#!/bin/bash

for r in {1..45}
do
  read -r -n 1 ori < dataset/sims3/gamespot/no$r.txt
  if [[ "$ori" =~ ^[0-9]+$ ]]
    then
     echo "$(tail -n +2 dataset/sims3/gamespot/no$r.txt)" > dataset/sims3/gamespot/no$r.txt
  else
    continue
  fi
done

for q in {1..45}
do
  read -r -n 1 wri < dataset/sims3/gamespot/yes$q.txt
  if [[ "$wri" =~ ^[0-9]+$ ]]
    then
     echo "$(tail -n +2 dataset/sims3/gamespot/yes$q.txt)" > dataset/sims3/gamespot/yes$q.txt
  else
    continue
  fi
done

for i in {1..45}
do
  read -r -n 1 ari < dataset/sims3/metacritic/no$i.txt
  if [[ "$ari" =~ ^[0-9]+$ ]]
    then
     echo "$(tail -n +2 dataset/sims3/metacritic/no$i.txt)" > dataset/sims3/metacritic/no$i.txt
  else
    continue
  fi
done

for x in {1..45}
do
  read -r -n 1 bri < dataset/sims3/metacritic/yes$x.txt
  if [[ "$bri" =~ ^[0-9]+$ ]]
    then
     echo "$(tail -n +2 dataset/sims3/metacritic/yes$x.txt)" > dataset/sims3/metacritic/yes$x.txt
  else
    continue
  fi
done

for y in {1..45}
do
  echo "$(tail -n +3 dataset/sims3/steam/no$y.txt)" > dataset/sims3/steam/no$y.txt
done

for z in {1..45}
do
  echo "$(tail -n +3 dataset/sims3/steam/yes$z.txt)" > dataset/sims3/steam/yes$z.txt
done